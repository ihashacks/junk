#!/usr/bin/python
#
#  20120524 by Brandon Pierce <brandon@ihashacks.com>
#
#  Dump the URL of the most recent entry in an atom feed.
#

import feedparser

feed = feedparser.parse('http://www.ihashacks.com/atom.xml')
print feed.feed.title+" "+'"'+feed.entries[0].title+'"'+" "+feed.entries[0].link
