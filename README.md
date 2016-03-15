# http://cesium.ml

## Installing build dependencies

```
pip install -r requirements.txt
git submodule init
git submodule update
```

## Editing the blog

- Update or add ``blog/content`` (see existing posts for examples)
- Run ``make devserver`` in blog, and connect to http://localhost:8000
- When ready to update blog, run ``tools/gh-upload.sh``

## Editing the main page

Edit ``gh-pages/index.html`` and preview in your browser.  When done, commit
the changes.

