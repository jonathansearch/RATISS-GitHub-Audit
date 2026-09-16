#!/bin/bash
# rejouer.sh — rejoue l'audit complet en une commande (R7).
#
#   repos.json ──> clones ──> audit.py ──> resultats-bruts.json
#                                   (reclassement.json = revue humaine)
#                                        └──> gen.py ──> resultats.json
#                                                         RAPPORT-GLOBAL.md
#
# N2 : le juge (RATISS-Framework) est tire du depot de reference possede
#      par jonathansearch, jamais d'un compte tiers.
set -euo pipefail
cd "$(dirname "$0")"

ORG="${RATISS_ORG:-jonathansearch}"
FRAMEWORK_REF="${RATISS_FRAMEWORK_REF:-https://github.com/jonathansearch/RATISS-Framework.git}"

# --- Garde anti-faux-rejeu : sans les outils, on echoue franchement ---------
missing=0
for f in audit.py gen.py reclassement.json; do
  [ -f "$f" ] || { echo "MANQUANT: $f — le rejeu ne peut pas etre honnete." >&2; missing=1; }
done
[ "$missing" -eq 0 ] || { echo "Rejeu refuse (R7)." >&2; exit 1; }

echo "== 1/5 Inventaire API =="
curl -s "https://api.github.com/users/${ORG}/repos?per_page=100" -o repos.json
python3 -c "import json;d=json.load(open('repos.json'));assert isinstance(d,list),d;print('repos:',len(d))"

echo "== 2/5 Clone des depots =="
rm -rf clones && mkdir clones
python3 -c "import json;[print(r['name']) for r in json.load(open('repos.json'))]" > names.txt
while read -r n; do
  git clone -q --depth 1 "https://github.com/${ORG}/${n}.git" "clones/$n" \
    && echo "OK   $n" || echo "FAIL $n"
done < names.txt

echo "== 3/5 Scan deterministe =="
python3 audit.py

echo "== 4/5 Reclassement humain + rapport =="
python3 gen.py

echo "== 5/5 Juge RATISS (depot de reference possede) =="
[ -d framework ] || git clone -q --depth 1 "$FRAMEWORK_REF" framework
if python3 -c "import pytest" 2>/dev/null; then
  python3 -m pytest framework -q 2>&1 | tail -1
else
  echo "(pytest absent — juge non execute, ce n'est PAS une conformite)"
fi

echo
echo "REJOUÉ. Voir RAPPORT-GLOBAL.md et resultats.json."
