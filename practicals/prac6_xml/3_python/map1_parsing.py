# -*- coding: utf-8 -*-
"""
For Advanced Programming practical 6: XML

Prints the tag names of xml file
"""

from lxml import etree

#Open the dtd file
dtd_file = open("map1.dtd")

# open the xml
xml1 = etree.parse("map1.xml")

#Loop through all elements of the xml
for element in xml1.iter():
    
    #print the name of the tag
    print(element.tag)

