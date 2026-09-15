# RATISS GitHub Audit

## Audit global du compte `jonathansearch`

Ce dépôt centralise l’audit professionnel du compte GitHub `jonathansearch`, exécuté selon la méthode de **RATISS-Framework**, couche 1 de RATISS Labs. Il sert de registre public des contrôles, des corrections non destructives, des suppressions confirmées et des décisions de conservation.

> **Périmètre.** L’audit s’appuie sur le rapport global daté du **2026-09-15**. Le rapport indique **45 dépôts audités**, une note moyenne de **77/100**, **3 dépôts de grade A**, **33 de grade B**, **9 de grade C**, **0 de grade D** et **0 de grade F**.

## Résumé exécutif

Le rapport identifie **0 vrai secret**, **0 vrai fichier `.env`** et **0 adresse email privée** dans le périmètre analysé. Le principal risque observé est la présentation publique : descriptions génériques, licences insuffisamment détectées par GitHub, dépôts copiés ou rebrandés, doublons de projets et quelques éléments de structure documentaire manquants.

Les dépôts `RATISS-Framework` et `RATISS-LABS-GTT` constituent les références techniques principales. Ils ont obtenu **100/100** dans le rapport. Le présent dépôt complète ces deux projets en documentant la gouvernance et l’hygiène publique du compte dans son ensemble.

## Actions confirmées exécutées

Les suppressions suivantes ont été demandées et confirmées par le propriétaire du compte, puis exécutées :

| Dépôt | Action | État |
|---|---|---|
| `open-webui` | suppression confirmée | supprimé |
| `ratiss-cypher-odv-scientist` | suppression confirmée | supprimé |
| `openhands` | suppression confirmée | supprimé |
| `robot-Ratiss-` | suppression confirmée | supprimé |
| `evinajonathan13-max` | suppression confirmée | supprimé |

Le site officiel retenu est **[ratiss-labs-site](https://jonathansearch.github.io/ratiss-labs-site/)**. Le dépôt doublon `ratiss-labs-website` a été **archivé**, et non supprimé, afin de conserver une option de récupération.

Le dépôt mal orthographié `sciece-2` a été renommé en [`science-2`](https://github.com/jonathansearch/science-2). Cette opération conserve l’historique du dépôt et bénéficie des redirections GitHub.

## Méthode RATISS-Framework

L’audit est documenté selon les principes R4 à R7 : les résultats sont séparés des hypothèses, les valeurs sont rattachées à leur périmètre, les écarts sont conservés et les affirmations doivent rester rejouables. Le rapport de référence précise que l’audit a été exécuté selon un processus de clone, scan, vérification des README, licences, secrets, fichiers volumineux, fichiers `.env` et auteurs, avec vérification humaine des indices sensibles.

Le dépôt de méthode est disponible dans [`RATISS-Framework`](https://github.com/jonathansearch/RATISS-Framework). La plateforme expérimentale correspondante est [`RATISS-LABS-GTT`](https://github.com/jonathansearch/RATISS-LABS-GTT).

## Liste des fichiers

| Fichier | Fonction |
|---|---|
| [`RAPPORT-GLOBAL.md`](RAPPORT-GLOBAL.md) | rapport global de l’audit du compte, avec scores, constats, limites et plan de correction |
| [`AUDIT.md`](AUDIT.md) | registre professionnel des contrôles exécutés, des décisions prises et des actions restantes |
| [`resultats.json`](resultats.json) | synthèse structurée des scores et catégories signalées dans le rapport |
| [`rejouer.sh`](rejouer.sh) | aide à la reproduction locale de l’audit et à la vérification des dépôts de référence |
| [`LICENSE`](LICENSE) | licence du présent registre documentaire |

Le présent registre est lui-même documenté comme un artefact audité par **RATISS-Framework**. Il ne remplace pas un audit indépendant : son statut est celui d’un auto-audit divulgué, conformément à la règle N2.

## Corrections non destructives

Les descriptions publiques des dépôts conservés sont normalisées pour éviter le libellé répétitif « RATISS Labs professional repository ». Les descriptions indiquent désormais le rôle du dépôt ou, lorsqu’aucune spécialisation fiable n’est disponible dans le rapport, son appartenance au portefeuille de recherche et d’ingénierie de RATISS Labs.

Les corrections futures recommandées concernent la présence de licences reconnues par GitHub, les README manquants, les fichiers `.gitignore`, la documentation des copies vendoriées et l’harmonisation des branches. Ces corrections doivent être appliquées dépôt par dépôt afin de ne pas modifier involontairement du code ou des preuves scientifiques.

## Limites déclarées

Le rapport source indique que les clones ont été effectués avec `--depth 1`. L’historique profond n’a donc pas été entièrement scanné. L’audit est un auto-audit exécuté avec les outils RATISS Labs ; la validation par un auditeur indépendant reste à obtenir.

## Contact et site officiel

Le site public de référence est [ratiss-labs-site](https://jonathansearch.github.io/ratiss-labs-site/). Le compte GitHub est [jonathansearch](https://github.com/jonathansearch). Le laboratoire RATISS Labs est présenté dans les dépôts de référence.

## Références

[1]: https://github.com/jonathansearch/RATISS-Framework "RATISS-Framework — protocole d’audit scientifique exécutable"
[2]: https://github.com/jonathansearch/RATISS-LABS-GTT "RATISS-LABS-GTT — plateforme expérimentale principale"
[3]: https://jonathansearch.github.io/ratiss-labs-site/ "Site officiel de RATISS Labs"
