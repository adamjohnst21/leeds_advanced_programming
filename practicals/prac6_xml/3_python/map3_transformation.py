# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:54:32 2018

@author: University
"""

from lxml import etree


# open the xml
xml1 = open("xml3.xml").read()

# remove the encoding declaration
xml1 = xml1.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
root = etree.XML(xml1)


xsl3 = open("map3.xsl").read()		# Read stylesheet
xsl3 = xsl3.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
xslt_root = etree.XML(xsl3)			# Parse stylesheet
transform = etree.XSLT(xslt_root)		# Make transform
result_tree = transform(root)			# Transform some XML root
transformed_text = str(result_tree)

print(transformed_text)
writer = open('map3.html', 'w')		# Normal writer
writer.write(transformed_text)
