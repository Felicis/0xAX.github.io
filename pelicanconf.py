# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'0xAX'
SITENAME = u'Just a Memo'
SITEURL = '0xax.github.com'
THEME = './pelican-bootstrap3'
PATH = 'content'

TIMEZONE = 'Asia/Omsk'

DEFAULT_LANG = u'en'

FEED_DOMAIN = None
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
HIDE_SIDEBAR=True

ADDTHIS_PROFILE = 'ra-53a535f822555b0c'
SHOW_ARTICLE_CATEGORY = True
DISQUS_ID_PREFIX_SLUG = True
DISQUS_DISPLAY_COUNTS = True
CC_LICENSE = 'CC-BY-NC'
DISQUS_SITENAME = '0xAX'
GOOGLE_ANALYTICS = 'UA-64079379-1'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = 10
FAVICON = 'extra/favicon.ico'
RELATIVE_URLS = True
PYGMENTS_STYLE = 'monokai'
GITHUB_USER = '0xAX'

STATIC_PATHS = [
    'extra'
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/github-8-24.gif': {'path': 'github-8-24.gif'},
    'extra/linkedin-3-24.jpg': {'path': 'linkedin-3-24.jpg'},
    'extra/stackoverflow-24.jpg': {'path': 'stackoverflow-24.jpg'},
    'extra/rss-24.gif': {'path': 'rss-24.gif'},
    'extra/archive-2-24.gif': {'path': 'archive-2-24.gif'},
    'extra/email-12-24.gif': {'path': 'email-12-24.gif'}
}

TWITTER_LOGO='twitter-24.gif'
GITHUB_LOGO='github-8-24.gif'
LINKEDIN_LOGO='linkedin-3-24.jpg'
STACKOVERFLOW_LOGO='stackoverflow-24.jpg'
RSS_LOGO='rss-24.gif'
ARCHIVES_LOGO='archive-2-24.gif'
EMAIL_LOGO='email-12-24.gif'
