#!/bin/sh
# Static build for Vercel (Framework Preset: Other, Build Command: sh build-static.sh, Output: dist).
# The case study is served at the SITE ROOT, so its relative asset paths (styles.css, app.js, ...)
# resolve to files that exist, and in-page "#section" links keep working. No rewrite or <base> needed.
#   dist/index.html, *.css, *.js   <- ui-prototype/
#   dist/dashboard/data.js         <- research data (window.DATA), loaded as /dashboard/data.js
#   dist/data/apps.json            <- app list, fetched as /data/apps.json
set -e

rm -rf dist
mkdir -p dist/dashboard dist/data

cp ui-prototype/index.html dist/index.html
cp ui-prototype/*.css dist/
for f in ui-prototype/*.js; do cp "$f" dist/; done

cp dashboard/data.js dist/dashboard/data.js
cp data/apps.json dist/data/apps.json

# fail the build if anything the page references is missing
for f in dist/index.html dist/styles.css dist/app.js dist/hero.js dist/skyline.js dist/glyph-bg.js dist/dashboard/data.js dist/data/apps.json; do
  [ -s "$f" ] || { echo "missing build output: $f" >&2; exit 1; }
done

echo "Static case study prepared in dist/ ($(ls dist | wc -l | tr -d ' ') top-level entries)."
