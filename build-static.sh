
#!/bin/sh
set -e

rm -rf dist

mkdir -p dist/ui-prototype
mkdir -p dist/dashboard
mkdir -p dist/data

cp ui-prototype/*.html dist/ui-prototype/
cp ui-prototype/*.js dist/ui-prototype/
cp ui-prototype/*.css dist/ui-prototype/

cp dashboard/data.js dist/dashboard/data.js
cp data/apps.json dist/data/apps.json

echo "Static case study prepared successfully."
