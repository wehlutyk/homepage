#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sébastien Lerique'
SITENAME = 'Sébastien Lerique'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Urls
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = 'posts/{date:%Y}-{date:%m}-{date:%d}-{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}-{date:%m}-{date:%d}-{slug}/index.html'

# Theme
THEME = 'pelicanyan'
TYPOGRIFY = True
MASTODON_ACCOUNT = 'mastodon.social/@wehlutyk'
TWITTER_ACCOUNT = 'wehlutyk'
GITHUB_ACCOUNT = 'wehlutyk'
GITLAB_ACCOUNT = 'wehlutyk'
EMAIL_ADDRESS = 'sl@slvh.fr'
MATRIX_ACCOUNT = 'sl:eauchat.org'
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives',
                    'sitemap', 'robots', 'humans')
ROBOTS_SAVE_AS = 'robots.txt'
HUMANS_SAVE_AS = 'humans.txt'
SITEMAP_SAVE_AS = 'sitemap.xml'
DEFAULT_LANG = 'en'
DATE_FORMATS = {'en': '%B %d, %Y'}
STATIC_PATHS = ['images', 'favicon.ico', 'static',
                # Copy a CNAME file for GitHub Pages
                'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

# Posts are drafts by default
DEFAULT_METADATA = {
    'status': 'draft',
}

# Blogroll
LINKS = (('Research', '/research/'),
         ('Tools', '/tools/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
