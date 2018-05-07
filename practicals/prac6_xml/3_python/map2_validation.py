# -*- coding: utf-8 -*-
"""
Created on Sun May  6 12:56:28 2018

@author: University
"""

from lxml import etree

xsd_file = open("map2.xsd")
xml2 = open("map2.xml").read()
xml2 = xml2.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
xsd = etree.XMLSchema(etree.parse(xsd_file))
root = etree.XML(xml2)
print(xsd.validate(root))
