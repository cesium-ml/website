#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Cesium Developers'
SITENAME = 'Cesium'
SITEURL = 'http://cesium-ml.org'

PATH = 'content'
RELATIVE_URLS = True
STATIC_PATHS = ['images', 'notebooks']

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/cesium-ml/cesium'),
          ('PyPi', 'https://pypi.python.org/pypi/cesium'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '../static/theme'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# The following markdown extension will remove any comments
# of the form <!---   text -->   (note the three opening dashes)
# from article input.
import sys, os
BASEDIR = os.path.join(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASEDIR, 'plugins_md/comments'))
from mkdcomments import CommentsExtension

sys.path.insert(0, os.path.join(BASEDIR, 'extensions'))

# https://github.com/getpelican/pelican/issues/1238
MD_EXTENSIONS = ['extra', 'sane_lists', 'smarty', 'toc',
                 CommentsExtension(),
                 'fenced_code',
                 'codehilite(css_class=highlight, linenums=False)']

FOUNDATION_PYGMENT_THEME = 'friendly'
