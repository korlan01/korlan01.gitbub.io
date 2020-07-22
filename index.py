#!/usr/bin/env python
# save as cgi-bin/index.py
# Python 2.7
import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()
html = """

try:
    length = int(form['length'].value)
    width = int(form['width'].value)
    area = length * width
    print "Content-Type: text/html"
    print 
    print "<p>The area is:  " + str(area) + "</p>"
except KeyError:
    print html