#!/bin/bash

set -e

THIS_DIR="$( dirname "${BASH_SOURCE[0]}")"
ROOT=$(cd "${THIS_DIR}/.." && pwd)

cd $ROOT/gh-pages
git fetch origin
git reset --hard origin/master
cp -r ../blog/output/* ./blog
git add .
git commit -m "Update blog"
git push origin master
