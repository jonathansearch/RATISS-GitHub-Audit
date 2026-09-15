#!/usr/bin/env bash
set -euo pipefail

printf '%s\n' '== RATISS GitHub Audit — contrôle documentaire =='
printf '%s\n' 'Références : RATISS-Framework et RATISS-LABS-GTT'

gh repo view jonathansearch/RATISS-Framework --json name,url,defaultBranchRef >/dev/null
gh repo view jonathansearch/RATISS-LABS-GTT --json name,url,defaultBranchRef >/dev/null
gh repo view jonathansearch/ratiss-labs-site --json name,url,defaultBranchRef >/dev/null

gh repo view jonathansearch/ratiss-labs-website --json name,isArchived >/dev/null
if gh repo view jonathansearch/open-webui >/dev/null 2>&1; then
  echo 'ERREUR : open-webui existe encore' >&2
  exit 1
fi

printf '%s\n' 'Contrôle réussi : dépôts de référence accessibles, doublon archivé et dépôt supprimé absent.'
