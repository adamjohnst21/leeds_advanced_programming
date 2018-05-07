# -*- coding: utf-8 -*-
"""
For Advanced Programming practical 5: Databases;

Read the database set up in createdb.py
"""

import sqlite3

#connect to the database
conn = sqlite3.connect('resultsdb.sqlite')

#Get a cursor from the connection, to interact with the database
c = conn.cursor()

# loop through each row in table and print the first value
for row in c.execute('SELECT * FROM Results ORDER BY burglaries'):
    print(u'{0}, {1}'.format(row[0], row[1]))