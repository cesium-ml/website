#!/bin/bash
THIS_DIR="$( dirname "${BASH_SOURCE[0]}")"
ROOT=$(cd "${THIS_DIR}/.." && pwd)

cd $ROOT/gh-pages
cp -r ../blog/output ./blog
git commit -am "Update blog"
git push origin master
