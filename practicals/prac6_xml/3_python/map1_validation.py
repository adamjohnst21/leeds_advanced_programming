# -*- coding: utf-8 -*-
"""
For Advanced Programming practical 6: XML

Validates map1.xml against DTD using lxml library
"""

from lxml import etree

#Open the dtd file
dtd_file = open("map1.dtd")

# open the xml
xml1 = open("map1.xml").read()

# remove the encoding declaration
xml1 = xml1.replace('<?xml version="1.0" encoding="UTF-8"?>',"")


dtd = etree.DTD(dtd_file)
root = etree.XML(xml1)


print(dtd.validate(root))
