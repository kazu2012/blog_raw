#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Brian Dant'
SITENAME = u'That I May "Live It"'
SITEURL = 'http://briandant.com'

TIMEZONE = 'America/New York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('@briandant', 'http://www.twitter.com/@briandant/'),
          ('LinkedIn', 'http://www.linkedin.com/in/briandant'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

OUTPUT_DIRECTORY = os.environ.get('BLOG_OUTPUT')
