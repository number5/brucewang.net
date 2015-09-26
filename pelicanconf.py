# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = u'Bruce Wang'
SITENAME = u'Bruce Wang - Simple, Love, Courage'
SITEURL = 'https://brucewang.net'
TIMEZONE = "Australia/Melbourne"

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


OUTPUT_PATH = 'public/'

DISQUS_SITENAME = "simplelovecourage"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_DATE = (2006, 11, 21, 14, 1, 1)

FEED_ALL_RSS = 'feeds/rss.xml'
USE_FOLDER_AS_CATEGORY = False

LINKS = ()

# global metadata to all the contents
DEFAULT_METADATA = {'yeah': 'it is'}

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    ]


DIRECT_TEMPLATES = ['index', 'archives']
# custom page generated with a jinja2 template
#TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}


THEME = 'crowsfoot'


GITHUB_ADDRESS = 'https://github.com/number5'
SO_ADDRESS = 'http://stackoverflow.com/users/29489/number5'
TWITTER_ADDRESS = 'https://twitter.com/number5'

#PROFILE_IMAGE_URL
LICENSE_URL = 'http://creativecommons.org/licenses/by-nc/4.0/'
LICENSE_NAME = 'Creative Commons Attribution-NonCommercial 4.0 International License'

SHOW_ARTICLE_AUTHOR = False

# URLS

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

# pagination
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/p/{number}/', '{base_name}/p/{number}/index.html'),
)


# tags 
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False


# plugins
PLUGINS = ['plugins.embed_tweet']

GOOGLE_ANALYTICS = 'UA-147870-2'

