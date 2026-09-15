# 🛡️ RAPPORT GLOBAL — Audit RATISS des 39 repos `jonathansearch` (v2 — contre-audit)

**Date :** 2026-09-15 — **Juge :** RATISS-Framework (couche 1, 47 tests passed, 4 skipped réseau)
**Méthode :** clone + scan (README, licence, secrets, gros fichiers, .env, auteurs) + vérification humaine de chaque indice secret.

## Verdict en 10 secondes
- **Note moyenne : 88/100** — Grades : A×33, B×4, C×2, D×0, F×0
- **Vrais secrets trouvés : 0** ✅ — **vrais .env : 0** ✅ — **emails privés : 0** ✅
- **Progrès : de flou (v1) à propre (v2).** Il reste ~20 min de finition (voir plan).

## 🎯 Les 7 failles invisibles (v2 : état actuel)
### 1. LICENCE-FLOUE — la tueuse de contrats (33 repos + 3 sans licence)
GitHub affiche **NOASSERTION** (licence inconnue) presque partout, même quand un fichier LICENSE existe. Pour une entreprise, NOASSERTION = *on ne touche pas*. Sans licence : `ratiss-audit-public`, `ratiss-labs-site`, `RATISS-GitHub-Audit`.
**Fix :** normaliser la licence (MIT comme tes flagships) → fixpack + PUSH_FIXPACK.sh.
### 2. DESC-GENERIQUE — ✅ CORRIGÉ (reste 1 : ratiss-labs-website)
En v1, 40 descriptions identiques. En v2, il ne reste que `ratiss-labs-website`. **Reste :** `bash fixpack/DESCRIPTIONS-RESTANTES.sh`.
### 3. COPIES-VENDORED — ✅ SUPPRIMÉES (4/4)
Rappel v1 : `open-webui` (155 Mo), `ratiss-cypher-odv-scientist` (164 Mo), `openhands`, `robot-Ratiss-` (LeRobot). Tous supprimés en v2 — risque réputation éliminé. **Conseil :** si besoin, refaire des vrais forks (bouton Fork).
### 4. MOTDEPASSE-TEST — la peur en public (1 repo)
`RATISS-ODV-AEON/tests/test_transdisc_security.py` : `CORRECT_PASSWORD = "Monnamour2008#"`. C'est une fixture de test, mais ça RESSEMBLE à un vrai mot de passe perso. **Fix :** 1 commande sed (fichier FIX-MOTDEPASSE-TEST.txt prêt).
### 5. NOMS — ✅ RENOMMÉ — reste : doublons (P1)
`sciece-2`→`science-2` renommé ✅, placeholders supprimés ✅. Reste (P1) : doublons `ratiss-bio` vs `RATISS-BIOLAB` et `ratiss-labs-site` vs `ratiss-labs-website` — fusionner puis archiver.
### 6. TROUS DE BASE — reste 1 README (ratiss-scientist-agent) + 5 .gitignore
1 README manquant (`ratiss-scientist-agent`, `ratiss-v1` supprimé ✅), 5 `.gitignore` manquants. **Fix :** fixpack prêt.
### 7. BRANCHE + AUTEURS — micro-désordre
`ratiss-labs-site` sur `master`, les autres sur `main`. 1 repo commité par `openhands@all-hands.dev` (`QPU-Ratiss-COSMOS`). Cosmetique, mais un auditeur le voit.

## ✅ Preuves d'honnêteté (ce qui N'EST PAS un problème)
- `sk-or-v1-...` dans 2 PROOF.md = placeholder tronqué, pas une clé.
- `sk-123456...` = fausse clé de test pour TON propre scanner (il la détecte ✅).
- `sk-diffusion-transformer-policy`, `sk-management` = noms de modèles, pas des clés.
- `.env.example` / `.env.sample` = exemples, bonne pratique.
- Aucun email privé dans les 45 histo.
- `RATISS-Framework` + `RATISS-LABS-GTT` déjà migrés sur jonathansearch : **100/100** 🏆

## 📊 Les 39 repos
| Repo | Score | Grade | Défaut principal |
|---|---|---|---|
| `RATISS-GitHub-Audit` | 65 | C | LICENCE-MANQUANTE |
| `ratiss-audit-public` | 65 | C | LICENCE-MANQUANTE |
| `ratiss-scientist-agent` | 75 | B | LICENCE-FLOUE |
| `science-2` | 75 | B | LICENCE-FLOUE |
| `ratiss-labs-site` | 78 | B | LICENCE-MANQUANTE |
| `ratiss-labs-website` | 80 | B | DESC-GENERIQUE |
| `RATISS-ODV-AEON` | 85 | A | LICENCE-FLOUE |
| `Travaux` | 85 | A | LICENCE-FLOUE |
| `ratiss-Skynet` | 85 | A | LICENCE-FLOUE |
| `Ratiss-experimental-IA-` | 86 | A | LICENCE-FLOUE |
| `Crypto-net-veo-` | 87 | A | LICENCE-FLOUE |
| `Ratiss-Jonathan-Labs-` | 89 | A | LICENCE-FLOUE |
| `Algorithmes-quantique-Ratiss-labs-` | 90 | A | LICENCE-FLOUE |
| `Porte-folio-Jonathan-` | 90 | A | LICENCE-FLOUE |
| `QPU-Ratiss-COSMOS` | 90 | A | LICENCE-FLOUE |
| `RATISS-BIOLAB` | 90 | A | LICENCE-FLOUE |
| `RATISS-GRID` | 90 | A | LICENCE-FLOUE |
| `RATISS-HPC` | 90 | A | LICENCE-FLOUE |
| `RATISS-QPU-AMBIENT` | 90 | A | LICENCE-FLOUE |
| `RATISS-V10-Physical-Complexity-Audit` | 90 | A | LICENCE-FLOUE |
| `Ratiss-Fusion-stark-` | 90 | A | LICENCE-FLOUE |
| `documentation-ia` | 90 | A | LICENCE-FLOUE |
| `quantum-circuit-studio` | 90 | A | LICENCE-FLOUE |
| `ratiss-aeon-agent` | 90 | A | LICENCE-FLOUE |
| `ratiss-aeon-model-runtime` | 90 | A | LICENCE-FLOUE |
| `ratiss-atelier` | 90 | A | LICENCE-FLOUE |
| `ratiss-bio` | 90 | A | LICENCE-FLOUE |
| `ratiss-colab-agent` | 90 | A | LICENCE-FLOUE |
| `ratiss-collapse-program` | 90 | A | LICENCE-FLOUE |
| `ratiss-cypher-odv-scientist-v2` | 90 | A | LICENCE-FLOUE |
| `ratiss-cypher-odv-scientist-v3` | 90 | A | LICENCE-FLOUE |
| `ratiss-decoherence-atlas` | 90 | A | LICENCE-FLOUE |
| `ratiss-labs-market-research` | 90 | A | LICENCE-FLOUE |
| `ratiss-lewm-integration` | 90 | A | LICENCE-FLOUE |
| `ratiss-topological-decoherence-engine` | 90 | A | LICENCE-FLOUE |
| `scientist-research-` | 90 | A | LICENCE-FLOUE |
| `RATISS-Framework` | 100 | A | OK |
| `RATISS-LABS-GTT` | 100 | A | OK |
| `metac-bot-template` | 100 | A | FORK |

## 📈 ÉVOLUTION — audit v1 (45 repos, 77/100) → contre-audit v2
- **Descriptions génériques : 40 → 1** (reste `ratiss-labs-website`) ✅
- **Supprimés : 8** — `open-webui`, `openhands`, `ratiss-cypher-odv-scientist`, `robot-Ratiss-`, `Naomi-Ia-`, `evinajonathan13-max`, `ratiss-v1`, `sciece-2`. Les 4 copies vendored ont disparu ✅
- **Renommé :** `sciece-2` → `science-2` ✅
- **Créé :** `RATISS-GitHub-Audit`, repo central des preuves ✅ (stratégie validée : mieux que 45 fichiers dispersés)

## 🔧 Plan — ce qui reste (P0, ~20 min)
1. Fix mot de passe test ODV-AEON (1 sed, fichier FIX-MOTDEPASSE-TEST.txt) + push.
2. `bash ratiss-audit/PUSH_FIXPACK.sh` (LICENSE + .gitignore + CITATION manquants).
3. `bash ratiss-audit/fixpack/DESCRIPTIONS-RESTANTES.sh` (1 description : `ratiss-labs-website`).
4. Mettre à jour `RATISS-GitHub-Audit` avec ce rapport v2 (RAPPORT-GLOBAL.md + resultats.json + rejouer.sh).
**P1 — cette semaine :** README pour `ratiss-scientist-agent`, décider doublons bio/BIOLAB + site/website, uniformiser MIT partout, `ratiss-labs-site` vers main.

## 📁 Fichiers livrés
- `per-repo/<nom>/AUDIT.md` — 39 preuves d'audit (artefacts, archivés ici + copiables dans RATISS-GitHub-Audit).
- `fixpack/<nom>/` — LICENSE / .gitignore / CITATION.cff manquants.
- `fixpack/DESCRIPTIONS-RESTANTES.sh` — la dernière description générique.
- `PUSH_FIXPACK.sh` — pousse le fixpack en une commande (sans spammer les repos).
- `resultats.json` — données brutes calculées (R4).
- `rejouer.sh` — **rejoue tout l'audit en une commande (R7).**

## ⚠️ Limites (honnêteté)
- Clones `--depth 1` : l'historique profond n'a pas été scanné.
- Aucun push effectué (pas tes identifiants) : les fix sont prêts, c'est toi qui pousses.
- Auto-audit divulgué : auditeur indépendant ⏳ EN ATTENTE (règle N2).

*MIT © 2026 Jonathan Evina, RATISS Labs — Yaoundé, Cameroun.*
