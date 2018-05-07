# -*- coding: utf-8 -*-
"""
For Advanced Programming practical 5: Databases;

Create and update the database

"""

import sqlite3

#connect to the database
conn = sqlite3.connect('resultsdb.sqlite')

print ("it's good to be back in python. #noMorePHP")

#Get a cursor from the connection, to interact with the database
c = conn.cursor()

#Create the table if running this for the first time
#c.execute("CREATE TABLE Results (address text, burglaries integer)")

# insert data
c.execute("INSERT INTO Results VALUES ('Queen Vic',2)")

# commit the changes
conn.commit()

#close the connection
conn.close()

