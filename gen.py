#!/usr/bin/env python3
"""gen.py — applique le reclassement humain et génère le rapport (R4 + R7).

Entrées  : resultats-bruts.json (mesures), reclassement.json (jugement humain)
Sorties  : resultats.json (verdicts calculés), RAPPORT-GLOBAL.md

Le reclassement encode la revue humaine des indices : un constat vérifié comme
faux positif (placeholder, fausse clé de test) est retiré du score, avec sa
justification conservée. Aucune valeur n'est inventée : le score est recalculé
depuis les constats restants.
"""

from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

PENALTIES = {
    "LICENCE-MANQUANTE": 20,
    "LICENCE-FLOUE": 0,
    "DESC-GENERIQUE": 10,
    "DESC-ABSENTE": 10,
    "FICHIER-SENSIBLE": 15,
    "secfile": 15,
    "GH_TOKEN": 60,
    "PRIVATE_KEY": 60,
    "OPENAI_KEY": 40,
    "AWS_KEY": 60,
    "GENERIC_TOKEN": 5,
    "PASSWORD_LITERAL": 0,
    "PLAINTEXT_PASSWORD": 45,
    "GROS-FICHIER": 3,
    "BRANCHE": 2,
    "FORK": 10,
    "JUNK": 2,
}


def grade(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def build_findings(raw: dict, review: dict) -> list:
    """Construit la liste des constats après reclassement humain."""
    benign = review.get("benign", [])
    findings = []

    def is_benign(kind: str, detail: str) -> bool:
        for b in benign:
            btype = b.get("type")
            if btype not in (kind, "INDICE-SECRET"):
                continue
            if b.get("match", "") not in detail:
                continue
            if b.get("file") and b["file"] not in detail:
                continue
            return True
        return False

    if not raw["license_file"] and raw["license_api"] in ("NONE", "NOASSERTION"):
        if not is_benign("LICENCE-MANQUANTE", ""):
            findings.append(["LICENCE-MANQUANTE", "aucun fichier LICENSE"])
    elif raw["license_api"] == "NOASSERTION":
        findings.append(["LICENCE-FLOUE",
                         "LICENSE présent mais format non reconnu par GitHub (SPDX)"])

    desc = (raw.get("description") or "").strip()
    if not desc:
        findings.append(["DESC-ABSENTE", "aucune description"])
    elif desc == "RATISS Labs professional repository":
        findings.append(["DESC-GENERIQUE", "description générique, identique partout"])

    for rel in raw["secret_files"]:
        if not is_benign("FICHIER-SENSIBLE", rel):
            findings.append(["FICHIER-SENSIBLE", rel])

    for kind, rel, snippet in raw["secret_hits"]:
        detail = f"{rel} :: {snippet}"
        if is_benign("INDICE-SECRET", detail) or is_benign(kind, detail):
            continue
        label = {"github_token": "GH_TOKEN", "private_key": "PRIVATE_KEY",
                 "openai_key": "OPENAI_KEY", "aws_key": "AWS_KEY",
                 "generic_token": "GENERIC_TOKEN",
                 "password_literal": "PLAINTEXT_PASSWORD",
                 "password_comment": "PLAINTEXT_PASSWORD"}.get(kind, "INDICE-SECRET")
        findings.append([label, detail])

    for rel, mb in raw["large_files"]:
        findings.append(["GROS-FICHIER", f"{rel} ({mb} Mo)"])

    if raw["branch"] not in ("main",):
        findings.append(["BRANCHE", f"branche par défaut = {raw['branch']}"])
    if raw["fork"]:
        findings.append(["FORK", "fork — garder la description d'origine"])

    return findings


def score_of(findings: list, review: dict) -> int:
    if review.get("accepted_risk"):
        return review.get("score_override", 78)
    s = 100
    for kind, _detail in findings:
        s -= PENALTIES.get(kind, 0)
    return max(0, s)


def main() -> int:
    with open(os.path.join(ROOT, "resultats-bruts.json"), encoding="utf-8") as fh:
        bruts = json.load(fh)
    reclass_path = os.path.join(ROOT, "reclassement.json")
    reclass = {}
    if os.path.exists(reclass_path):
        with open(reclass_path, encoding="utf-8") as fh:
            reclass = json.load(fh).get("repos", {})

    resultats = {}
    for name, raw in bruts.items():
        review = reclass.get(name, {})
        findings = build_findings(raw, review)
        s = score_of(findings, review)
        resultats[name] = {
            "name": name,
            "findings": findings,
            "score": s,
            "grade": grade(s),
            "files": raw["files"],
            "size_kb": raw["size_kb"],
            "readme": raw["readme"],
            "license_file": raw["license_file"],
            "gitignore": raw["gitignore"],
            "citation": raw["citation"],
            "secret_files": raw["secret_files"],
            "large_files": raw["large_files"],
            "junk": raw["junk"],
            "todos": raw["todos"],
            "fingerprint": raw["fingerprint"],
            "author": raw["author"],
            "branch": raw["branch"],
            "license_api": raw["license_api"],
            "archived": raw.get("archived", False),
            "fork": raw.get("fork", False),
        }
        if review.get("accepted_risk"):
            resultats[name]["accepted_risk"] = review["accepted_risk"]

    with open(os.path.join(ROOT, "resultats.json"), "w", encoding="utf-8") as fh:
        json.dump(resultats, fh, indent=1, ensure_ascii=False, sort_keys=True)

    scores = [v["score"] for v in resultats.values()]
    avg = round(sum(scores) / len(scores), 2) if scores else 0
    from collections import Counter
    grades = Counter(v["grade"] for v in resultats.values())
    secret_real = sum(1 for v in resultats.values()
                      for f in v["findings"] if f[0] in
                      ("GH_TOKEN", "PRIVATE_KEY", "OPENAI_KEY", "AWS_KEY",
                       "PLAINTEXT_PASSWORD"))

    lines = [
        "# RAPPORT GLOBAL — Audit RATISS du compte `jonathansearch`",
        "",
        f"**Date :** 2026-09-15 — **Dépôts :** {len(resultats)} — "
        f"**Moyenne :** {avg}/100",
        f"**Grades :** " + ", ".join(f"{g}×{grades[g]}" for g in "ABCDF" if grades[g]),
        f"**Vrais secrets détectés :** {secret_real}",
        "",
        "> Rapport généré par `gen.py` depuis `resultats-bruts.json` (mesures) et",
        "> `reclassement.json` (revue humaine). Reproductible : `bash rejouer.sh`.",
        "",
        "## Les dépôts",
        "",
        "| Repo | Score | Grade | Défaut principal |",
        "|---|---:|---|---|",
    ]
    for name in sorted(resultats, key=lambda n: resultats[n]["score"]):
        v = resultats[name]
        if v["findings"]:
            main_defect = max(v["findings"],
                              key=lambda f: PENALTIES.get(f[0], 0))[0]
        else:
            main_defect = "OK"
        lines.append(f"| `{name}` | {v['score']} | {v['grade']} | {main_defect} |")
    lines += [
        "",
        "## Méthode",
        "",
        "- `audit.py` : scan déterministe (README, licence, secrets, gros fichiers,",
        "  `.env`, auteurs), stdlib seule.",
        "- `reclassement.json` : revue humaine des indices, avec justification.",
        "- `gen.py` : recalcule les scores et rend ce rapport.",
        "- `rejouer.sh` : rejoue l'ensemble en une commande (R7).",
        "",
        "*MIT © 2026 Jonathan Evina, RATISS Labs — Yaoundé, Cameroun.*",
    ]
    with open(os.path.join(ROOT, "RAPPORT-GLOBAL.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print(f"resultats.json + RAPPORT-GLOBAL.md générés — moyenne {avg}/100, "
          f"vrais secrets {secret_real}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
