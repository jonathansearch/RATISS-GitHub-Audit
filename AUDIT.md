# Registre d’audit GitHub — `jonathansearch`

**Date de référence :** 2026-09-15  
**Méthode :** RATISS-Framework, couche 1  
**Nature :** auto-audit divulgué ; validation indépendante en attente

## Verdict global

Le rapport source couvre **45 dépôts** et attribue une note moyenne de **77/100**. La distribution annoncée est de **3 grades A**, **33 grades B**, **9 grades C**, **0 grade D** et **0 grade F**. Les contrôles de sécurité indiquent **0 vrai secret**, **0 vrai fichier `.env`** et **0 email privé**.

## Actions exécutées

Les dépôts `open-webui`, `ratiss-cypher-odv-scientist`, `openhands`, `robot-Ratiss-` et `evinajonathan13-max` ont été supprimés après confirmation explicite du propriétaire. Le dépôt `ratiss-labs-website` a été archivé afin de préserver une possibilité de récupération. Le dépôt `sciece-2` a été renommé `science-2`. Le site officiel conservé est `ratiss-labs-site`.

## Actions non destructives recommandées

Les descriptions génériques doivent être remplacées par des descriptions propres à chaque projet. Les licences doivent être rendues détectables par GitHub lorsque le contenu et les conditions du dépôt le permettent. Les dépôts sans README ou `.gitignore` doivent être complétés. Les copies de composants tiers doivent porter un fichier `NOTICE-COPIE.md` ou être clairement identifiées comme forks. La branche `master` de `ratiss-labs-site` peut être harmonisée vers `main` après vérification du déploiement du site.

## Intégrité et limites

L’audit source a utilisé des clones superficiels `--depth 1`. Il ne constitue donc pas une analyse exhaustive de tout l’historique Git. Les indices signalés comme secrets ont fait l’objet d’une vérification humaine selon le rapport. La conformité technique ne constitue pas une validation scientifique indépendante.

## Références

[1]: https://github.com/jonathansearch/RATISS-Framework "RATISS-Framework — protocole d’audit scientifique exécutable"
[2]: https://github.com/jonathansearch/RATISS-LABS-GTT "RATISS-LABS-GTT — plateforme expérimentale principale"
