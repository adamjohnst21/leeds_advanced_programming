# -*- coding: utf-8 -*-
"""
For Advanced Programming practical 6: XML

Prints the tag names of xml file
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

p2 = etree.Element("polygon")				# Create polygon
p2.set("id", "p2");					# Set attribute
p2.append(etree.Element("points"))			# Append points
p2[0].text = "100,100 100,200 200,200 200,100"	# Set points text
root.append(p2)						# Append polygon
print (root[1].tag)					# Check

out = etree.tostring(root, pretty_print=True)
print(out)
writer = open('xml3.xml', 'wb')		# Open for binary write
writer.write(out)
writer.close()
