#!/bin/bash

set -e

THIS_DIR="$( dirname "${BASH_SOURCE[0]}")"
ROOT=$(cd "${THIS_DIR}/.." && pwd)

cd $ROOT/gh-pages
git checkout master
git fetch origin
git reset --hard origin/master
git clean -xdf

cd $ROOT/blog
make publish

cd $ROOT/gh-pages
git add .
git commit -m "Update website"
git push origin master
