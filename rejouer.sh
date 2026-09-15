#!/bin/bash
# R7 — rejoue TOUT l'audit en une commande.
set -e
cd "$(dirname "$0")"
curl -s "https://api.github.com/users/jonathansearch/repos?per_page=100" -o repos.json
[ -d framework ] || git clone --depth 1 https://github.com/brossbernard2-pixel/RATISS-Framework.git framework
python3 -m pytest framework -q 2>&1 | tail -1
rm -rf clones && mkdir clones
python3 -c "import json; [print(r['name']) for r in json.load(open('repos.json'))]" > names.txt
while read -r n; do git clone -q --depth 1 "https://github.com/jonathansearch/$n.git" "clones/$n" && echo "OK $n"; done < names.txt
python3 audit.py > audit-console.txt
python3 gen.py
echo "REJOUE TERMINE — voir RAPPORT-GLOBAL.md"
