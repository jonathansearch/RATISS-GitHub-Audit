# RAPPORT GLOBAL — Audit RATISS du compte `jonathansearch`

**Date :** 2026-09-15 — **Dépôts :** 39 — **Moyenne :** 93.1/100
**Grades :** A×35, C×2, F×2
**Vrais secrets détectés :** 5

> Rapport généré par `gen.py` depuis `resultats-bruts.json` (mesures) et
> `reclassement.json` (revue humaine). Reproductible : `bash rejouer.sh`.

## Les dépôts

| Repo | Score | Grade | Défaut principal |
|---|---:|---|---|
| `ratiss-aeon-agent` | 0 | F | PLAINTEXT_PASSWORD |
| `RATISS-ODV-AEON` | 10 | F | PLAINTEXT_PASSWORD |
| `metac-bot-template` | 70 | C | LICENCE-MANQUANTE |
| `ratiss-labs-site` | 78 | C | LICENCE-MANQUANTE |
| `ratiss-labs-website` | 90 | A | DESC-GENERIQUE |
| `Ratiss-experimental-IA-` | 94 | A | GROS-FICHIER |
| `ratiss-scientist-agent` | 95 | A | GENERIC_TOKEN |
| `Crypto-net-veo-` | 97 | A | GROS-FICHIER |
| `Ratiss-Jonathan-Labs-` | 97 | A | GROS-FICHIER |
| `Algorithmes-quantique-Ratiss-labs-` | 100 | A | LICENCE-FLOUE |
| `Porte-folio-Jonathan-` | 100 | A | LICENCE-FLOUE |
| `QPU-Ratiss-COSMOS` | 100 | A | LICENCE-FLOUE |
| `RATISS-BIOLAB` | 100 | A | LICENCE-FLOUE |
| `RATISS-Framework` | 100 | A | OK |
| `RATISS-GRID` | 100 | A | LICENCE-FLOUE |
| `RATISS-GitHub-Audit` | 100 | A | OK |
| `RATISS-HPC` | 100 | A | LICENCE-FLOUE |
| `RATISS-LABS-GTT` | 100 | A | OK |
| `RATISS-QPU-AMBIENT` | 100 | A | LICENCE-FLOUE |
| `RATISS-V10-Physical-Complexity-Audit` | 100 | A | LICENCE-FLOUE |
| `Ratiss-Fusion-stark-` | 100 | A | LICENCE-FLOUE |
| `Travaux` | 100 | A | LICENCE-FLOUE |
| `documentation-ia` | 100 | A | LICENCE-FLOUE |
| `quantum-circuit-studio` | 100 | A | LICENCE-FLOUE |
| `ratiss-Skynet` | 100 | A | LICENCE-FLOUE |
| `ratiss-aeon-model-runtime` | 100 | A | LICENCE-FLOUE |
| `ratiss-atelier` | 100 | A | LICENCE-FLOUE |
| `ratiss-audit-public` | 100 | A | OK |
| `ratiss-bio` | 100 | A | LICENCE-FLOUE |
| `ratiss-colab-agent` | 100 | A | LICENCE-FLOUE |
| `ratiss-collapse-program` | 100 | A | LICENCE-FLOUE |
| `ratiss-cypher-odv-scientist-v2` | 100 | A | LICENCE-FLOUE |
| `ratiss-cypher-odv-scientist-v3` | 100 | A | LICENCE-FLOUE |
| `ratiss-decoherence-atlas` | 100 | A | LICENCE-FLOUE |
| `ratiss-labs-market-research` | 100 | A | LICENCE-FLOUE |
| `ratiss-lewm-integration` | 100 | A | LICENCE-FLOUE |
| `ratiss-topological-decoherence-engine` | 100 | A | LICENCE-FLOUE |
| `science-2` | 100 | A | LICENCE-FLOUE |
| `scientist-research-` | 100 | A | LICENCE-FLOUE |

## Méthode

- `audit.py` : scan déterministe (README, licence, secrets, gros fichiers,
  `.env`, auteurs), stdlib seule.
- `reclassement.json` : revue humaine des indices, avec justification.
- `gen.py` : recalcule les scores et rend ce rapport.
- `rejouer.sh` : rejoue l'ensemble en une commande (R7).

*MIT © 2026 Jonathan Evina, RATISS Labs — Yaoundé, Cameroun.*
