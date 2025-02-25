#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Greg Lindahl'
SITENAME = 'ngEHT Analysis Challenge'
SITEURL = ''

STATIC_URL = '{path}'
STATIC_PATHS = ['static', '', 'c1downloads', 'scripts']
STATIC_CREATE_LINKS = True  # because of the large data files in static
# but I never figured out how to talk rsync into hard linking them

PATH = 'content'
PAGE_PATHS = ['']
ARTICLE_PATHS = []
#ARTICLE_PATHS = ['examples']
#ARTICLE_EXCLUDES = ['examples/authors', 'examples/categories', 'examples/tags']

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# causes a "unsupported locale setting" ... challenge doesn't have dated articles anyway
#DATE_FORMATS = {'en': ('en_US.UTF-8', '%b %d, %Y')}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None
#LINKS_WIDGET_NAME=''

# Social widget -- bottom right
SOCIAL = False
#SOCIAL_WIDGET_NAME=''

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (('C#1', '/challenge1/'),
             ('C#2', '/challenge2/'),
             ('C#3', '/challenge3/'),
             ('Challenge #4', '/challenge4/'),
             ('Installing', '/installing/'),
             ('FAQ', '/faq/'),
             ('Credits', '/credits/'),)

THEME_TEMPLATES_OVERRIDES = ['content/templates']  # works for base.html override
PAGE_EXCLUDES = ['templates', 'static']
INDEX_SAVE_AS = 'standard_index.html'

DEFAULT_PAGINATION = False

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
#ARCHIVES_URL = 'examples/'
#ARCHIVES_SAVE_AS = 'examples/index.html'
#ARTICLE_URL = '{slug}/' # category is part of the slug (i.e., examples)
#ARTICLE_SAVE_AS = '{slug}/index.html'
#AUTHOR_URL = 'author/{slug}/'
#AUTHOR_SAVE_AS = 'author/{slug}/index.html'
#CATEGORY_URL = 'category/{slug}/'
#CATEGORY_SAVE_AS = 'category/{slug}/index.html'
#TAG_URL = 'tag/{slug}/'
#TAG_SAVE_AS = 'tag/{slug}/index.html'

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
}

AUTHORS_SAVE_AS = None # Not used
CATEGORIES_SAVE_AS = None # Not used
TAGS_SAVE_AS = None # Not used

SLUGIFY_SOURCE = 'basename'
PATH_METADATA = '(?P<slug>.+).rst'

# pip install pelican-render-math puts this in the right place
# ditto for pelican-just-table
PLUGINS = ["render_math", 'pelican_just_table']

# moved here because I'm not using "make publish"
GOOGLE_ANALYTICS = "G-VQ1E29BE8K"
