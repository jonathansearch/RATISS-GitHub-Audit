#!/usr/bin/env python3
"""audit.py — scan déterministe des dépôts clonés (R4 : valeurs calculées).

Lit `repos.json` (inventaire API) et `clones/<nom>/`, produit
`resultats-bruts.json`. Aucune décision humaine ici : uniquement des constats
mesurés. Les faux positifs sont traités séparément dans `reclassement.json`
par `gen.py`, afin que le jugement humain reste explicite et traçable.

Stdlib uniquement. Sortie : resultats-bruts.json
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CLONES = os.path.join(ROOT, "clones")

LARGE_FILE_MB = 5.0
MAX_SCAN_BYTES = 512 * 1024  # on ne lit pas les très gros fichiers en entier

SECRET_FILE_NAMES = {
    ".env", ".env.local", ".env.production", ".env.development",
    "id_rsa", "id_ed25519", ".npmrc", ".pypirc",
}
SECRET_FILE_SUFFIXES = (".pem", ".key", ".pfx", ".p12")

SECRET_PATTERNS = [
    ("github_token", re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}")),
    ("openai_key", re.compile(r"sk-[A-Za-z0-9]{20,}")),
    ("private_key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("aws_key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("generic_token", re.compile(
        r"(?i)(api[_-]?key|secret|token|password|passwd)\s*[:=]\s*"
        r"['\"][^'\"]{6,}['\"]")),
    ("password_literal", re.compile(
        r"(?i)password\s*[:=]\s*[\"']([^\"'\n]{8,})[\"']")),
    ("password_comment", re.compile(
        r"(?i)mot de passe[^\n]{0,60}?\"([^\"\n]{8,})\"")),
]

# Valeurs manifestement non sensibles (placeholders, doc, exemples).
PLACEHOLDER_RE = re.compile(
    r"(?i)(votre|your|xxx|placeholder|changeme|example|exemple|test|dummy|"
    r"passer|motdepasse|admin|<.*>|toto|\.\.\.|•)")


def _looks_like_placeholder(value: str) -> bool:
    if re.fullmatch(r"[a-z_][a-z0-9_]*", value):  # identifiant, pas un littéral
        return True
    return bool(PLACEHOLDER_RE.search(value))

JUNK_NAMES = {"__pycache__", ".DS_Store", "node_modules", ".pytest_cache",
              ".mypy_cache", ".ipynb_checkpoints"}
GENERIC_DESC = "RATISS Labs professional repository"


def _read_text(path: str) -> str:
    try:
        with open(path, "rb") as fh:
            return fh.read(MAX_SCAN_BYTES).decode("utf-8", "ignore")
    except OSError:
        return ""


def _last_author(repo_dir: str) -> str:
    try:
        out = subprocess.run(
            ["git", "-C", repo_dir, "log", "-1", "--format=%an <%ae> | %ad",
             "--date=short"],
            capture_output=True, text=True, timeout=20,
        )
        return out.stdout.strip() or "inconnu"
    except Exception:
        return "inconnu"


def scan_repo(name: str, api: dict) -> dict:
    repo_dir = os.path.join(CLONES, name)
    files = []
    total = 0
    for dirpath, dirnames, filenames in os.walk(repo_dir):
        if ".git" in dirnames:
            dirnames.remove(".git")
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, repo_dir)
            files.append(rel)
            try:
                total += os.path.getsize(full)
            except OSError:
                pass

    root_files = [f for f in files if "/" not in f]
    root_lower = {f.lower() for f in root_files}

    readme = any(f.startswith("readme") for f in root_lower)
    license_file = any(f.startswith(("license", "licence", "copying"))
                       for f in root_lower)
    gitignore = ".gitignore" in root_lower
    citation = any(f.startswith("citation") for f in root_lower)

    secret_files, secret_hits, large_files, junk = [], [], [], []
    todos = 0

    for rel in files:
        base = os.path.basename(rel)
        full = os.path.join(repo_dir, rel)

        if base in SECRET_FILE_NAMES or rel.lower().endswith(SECRET_FILE_SUFFIXES):
            secret_files.append(rel)
        if base in JUNK_NAMES:
            junk.append(rel)

        try:
            size_mb = os.path.getsize(full) / (1024 * 1024)
        except OSError:
            continue
        if size_mb >= LARGE_FILE_MB:
            large_files.append([rel, round(size_mb, 1)])
            continue  # pas de scan de secret dans un gros binaire

        if base.endswith((".py", ".md", ".txt", ".json", ".ts", ".tsx", ".js",
                          ".yml", ".yaml", ".toml", ".cfg", ".ini", ".sh", ".cff")):
            text = _read_text(full)
            todos += len(re.findall(r"\bTODO\b|\bFIXME\b", text))
            for kind, pat in SECRET_PATTERNS:
                for m in pat.finditer(text):
                    value = m.group(1) if m.groups() else m.group(0)
                    if kind in ("password_literal", "password_comment"):
                        if _looks_like_placeholder(value):
                            continue
                        snippet = value[:16]
                    else:
                        snippet = m.group(0)[:12]
                    secret_hits.append([kind, rel, snippet])

    fs = sorted(files)
    fingerprint = hashlib.md5("\n".join(fs).encode()).hexdigest()[:16]

    return {
        "name": name,
        "files": len(files),
        "size_kb": round(total / 1024),
        "readme": readme,
        "license_file": license_file,
        "gitignore": gitignore,
        "citation": citation,
        "secret_files": secret_files,
        "secret_hits": secret_hits[:40],
        "large_files": large_files,
        "junk": junk[:40],
        "todos": todos,
        "fingerprint": fingerprint,
        "author": _last_author(repo_dir),
        "branch": api.get("default_branch", "?"),
        "license_api": (api.get("license") or {}).get("spdx_id", "NONE"),
        "description": api.get("description") or "",
        "fork": bool(api.get("fork")),
        "archived": bool(api.get("archived")),
    }


def main() -> int:
    if not os.path.isdir(CLONES):
        print("clones/ absent — lancer d'abord le clone", file=sys.stderr)
        return 1
    with open(os.path.join(ROOT, "repos.json"), encoding="utf-8") as fh:
        api_repos = {r["name"]: r for r in json.load(fh)}

    results = {}
    for name in sorted(os.listdir(CLONES)):
        if not os.path.isdir(os.path.join(CLONES, name)):
            continue
        results[name] = scan_repo(name, api_repos.get(name, {}))

    out = os.path.join(ROOT, "resultats-bruts.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=1, ensure_ascii=False, sort_keys=True)
    print(f"{len(results)} dépôts scannés -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
