# 🛡️ RAPPORT GLOBAL — Audit RATISS des 45 repos `jonathansearch`

**Date :** 2026-09-15 — **Juge :** RATISS-Framework (couche 1, 47 tests passed, 4 skipped réseau)
**Méthode :** clone + scan (README, licence, secrets, gros fichiers, .env, auteurs) + vérification humaine de chaque indice secret.

## Verdict en 10 secondes
- **Note moyenne : 77/100** — Grades : A×3, B×33, C×9, D×0, F×0
- **Vrais secrets trouvés : 0** ✅ — **vrais .env : 0** ✅ — **emails privés : 0** ✅
- **Ton GitHub n'est PAS sale. Il est flou.** Et le flou fait peur aux entreprises. On corrige ça.

## 🎯 Les 7 failles invisibles (les plus attirantes)
### 1. LICENCE-FLOUE — la tueuse de contrats (40 repos)
GitHub affiche **NOASSERTION** (licence inconnue) presque partout, même quand un fichier LICENSE existe. Pour une entreprise, NOASSERTION = *on ne touche pas*. jewelry.
**Fix :** normaliser la licence (MIT comme tes flagships) → fixpack + PUSH_AUDITS.sh.
### 2. DESC-GENERIQUE — l'air de faux (40 repos)
La description About dit partout *RATISS Labs professional repository*. Un client qui voit 40 fois la même phrase pense *bot*. **Fix :** `bash fixpack/DESCRIPTIONS.sh` (40 vraies descriptions prêtes).
### 3. COPIES-VENDORED — 300 Mo + risque réputation (4 repos)
`open-webui` (155 Mo), `ratiss-cypher-odv-scientist` (164 Mo, contient une 2e copie d'Open WebUI !), `openhands` (21 Mo, logo remplacé par RATISS), `robot-Ratiss-` (contient LeRobot). Licence d'origine conservée ✅ mais rebrandées. Un client peut croire que tu t'attribues leur travail.
**Fix :** ajouter NOTICE-COPIE.md (prêt) OU supprimer et faire de vrais forks.
### 4. MOTDEPASSE-TEST — la peur en public (1 repo)
`RATISS-ODV-AEON/tests/test_transdisc_security.py` : `CORRECT_PASSWORD = "Monnamour2008#"`. C'est une fixture de test, mais ça RESSEMBLE à un vrai mot de passe perso. **Fix :** 1 commande sed (fichier FIX-MOTDEPASSE-TEST.txt prêt).
### 5. NOMS + DOUBLONS — le désordre visible
`sciece-2` (faute : science), `evinajonathan13-max` (placeholder), `ratiss-labs-website` vs `ratiss-labs-site` (doublon), `ratiss-bio` vs `RATISS-BIOLAB` (doublon ?). **Fix :** renommer (Settings → Rename, GitHub redirige tout seul), archiver les doublons.
### 6. TROUS DE BASE — README / .gitignore
2 README manquants (`ratiss-scientist-agent`, `ratiss-v1`), 6 `.gitignore` manquants. **Fix :** fixpack prêt.
### 7. BRANCHE + AUTEURS — micro-désordre
`ratiss-labs-site` sur `master`, les autres sur `main`. 1 repo commité par `openhands@all-hands.dev` (`QPU-Ratiss-COSMOS`). Cosmetique, mais un auditeur le voit.

## ✅ Preuves d'honnêteté (ce qui N'EST PAS un problème)
- `sk-or-v1-...` dans 2 PROOF.md = placeholder tronqué, pas une clé.
- `sk-123456...` = fausse clé de test pour TON propre scanner (il la détecte ✅).
- `sk-diffusion-transformer-policy`, `sk-management` = noms de modèles, pas des clés.
- `.env.example` / `.env.sample` = exemples, bonne pratique.
- Aucun email privé dans les 45 historiques (noreply partout).
- `RATISS-Framework` + `RATISS-LABS-GTT` déjà migrés sur jonathansearch : **100/100** 🏆

## 📊 Les 45 repos
| Repo | Score | Grade | Défaut principal |
|---|---|---|---|
| `ratiss-cypher-odv-scientist` | 53 | C | DESC-GENERIQUE |
| `open-webui` | 54 | C | DESC-GENERIQUE |
| `evinajonathan13-max` | 60 | C | DESC-GENERIQUE |
| `robot-Ratiss-` | 60 | C | DESC-GENERIQUE |
| `sciece-2` | 60 | C | DESC-GENERIQUE |
| `openhands` | 64 | C | DESC-GENERIQUE |
| `ratiss-audit-public` | 65 | C | LICENCE-MANQUANTE |
| `ratiss-scientist-agent` | 65 | C | DESC-GENERIQUE |
| `ratiss-v1` | 65 | C | DESC-GENERIQUE |
| `Naomi-Ia-` | 75 | B | DESC-GENERIQUE |
| `RATISS-ODV-AEON` | 75 | B | DESC-GENERIQUE |
| `Travaux` | 75 | B | DESC-GENERIQUE |
| `ratiss-Skynet` | 75 | B | DESC-GENERIQUE |
| `Ratiss-experimental-IA-` | 76 | B | DESC-GENERIQUE |
| `Crypto-net-veo-` | 77 | B | DESC-GENERIQUE |
| `ratiss-labs-site` | 78 | B | LICENCE-MANQUANTE |
| `Ratiss-Jonathan-Labs-` | 79 | B | DESC-GENERIQUE |
| `Algorithmes-quantique-Ratiss-labs-` | 80 | B | DESC-GENERIQUE |
| `Porte-folio-Jonathan-` | 80 | B | DESC-GENERIQUE |
| `QPU-Ratiss-COSMOS` | 80 | B | DESC-GENERIQUE |
| `RATISS-BIOLAB` | 80 | B | DESC-GENERIQUE |
| `RATISS-GRID` | 80 | B | DESC-GENERIQUE |
| `RATISS-HPC` | 80 | B | DESC-GENERIQUE |
| `RATISS-QPU-AMBIENT` | 80 | B | DESC-GENERIQUE |
| `RATISS-V10-Physical-Complexity-Audit` | 80 | B | DESC-GENERIQUE |
| `Ratiss-Fusion-stark-` | 80 | B | DESC-GENERIQUE |
| `documentation-ia` | 80 | B | DESC-GENERIQUE |
| `quantum-circuit-studio` | 80 | B | DESC-GENERIQUE |
| `ratiss-aeon-agent` | 80 | B | DESC-GENERIQUE |
| `ratiss-aeon-model-runtime` | 80 | B | DESC-GENERIQUE |
| `ratiss-atelier` | 80 | B | DESC-GENERIQUE |
| `ratiss-bio` | 80 | B | DESC-GENERIQUE |
| `ratiss-colab-agent` | 80 | B | DESC-GENERIQUE |
| `ratiss-collapse-program` | 80 | B | DESC-GENERIQUE |
| `ratiss-cypher-odv-scientist-v2` | 80 | B | DESC-GENERIQUE |
| `ratiss-cypher-odv-scientist-v3` | 80 | B | DESC-GENERIQUE |
| `ratiss-decoherence-atlas` | 80 | B | DESC-GENERIQUE |
| `ratiss-labs-market-research` | 80 | B | DESC-GENERIQUE |
| `ratiss-labs-website` | 80 | B | DESC-GENERIQUE |
| `ratiss-lewm-integration` | 80 | B | DESC-GENERIQUE |
| `ratiss-topological-decoherence-engine` | 80 | B | DESC-GENERIQUE |
| `scientist-research-` | 80 | B | DESC-GENERIQUE |
| `RATISS-Framework` | 100 | A | OK |
| `RATISS-LABS-GTT` | 100 | A | OK |
| `metac-bot-template` | 100 | A | FORK |

## 🔧 Plan de correction
**P0 — 30 min, faire aujourd'hui :**
1. `gh auth login` puis `bash ratiss-audit/fixpack/DESCRIPTIONS.sh` (descriptions).
2. `bash ratiss-audit/PUSH_AUDITS.sh` (AUDIT.md + LICENSE + .gitignore + CITATION partout).
3. Fix mot de passe test (1 sed) + push.
**P1 — cette semaine :** renommer `sciece-2`, décider `evinajonathan13-max`, NOTICE sur les 4 copies OU suppression, README pour les 2 manquants.
**P2 — optionnel :** fusionner doublons bio/BIOLAB + site/website, uniformiser MIT partout, passer `ratiss-labs-site` sur main.

## 📁 Fichiers livrés
- `per-repo/<nom>/AUDIT.md` — 45 preuves d'audit, une par repo (à committer).
- `fixpack/<nom>/` — LICENSE / .gitignore / CITATION.cff / NOTICE manquants.
- `fixpack/DESCRIPTIONS.sh` — 40 vraies descriptions About.
- `PUSH_AUDITS.sh` — pousse tout en une commande.
- `resultats.json` — données brutes calculées (R4).
- `rejouer.sh` — **rejoue tout l'audit en une commande (R7).**

## ⚠️ Limites (honnêteté)
- Clones `--depth 1` : l'historique profond n'a pas été scanné.
- Aucun push effectué (pas tes identifiants) : les fix sont prêts, c'est toi qui pousses.
- Auto-audit divulgué : auditeur indépendant ⏳ EN ATTENTE (règle N2).

*MIT © 2026 Jonathan Evina, RATISS Labs — Yaoundé, Cameroun.*
