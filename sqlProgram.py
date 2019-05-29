# -*- coding: utf-8 -*-
"""
Created on Mon May 27 10:39:14 2019

@author: Shraddha
"""

import sqlite3

con = sqlite3.connect('music.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS album')
cur.execute('CREATE TABLE album(singer text, tracks integer)')

cur.execute('''INSERT INTO album values
            ('Justin Beiber',2),
            ('Selena Gomez',10), 
            ('Justin Bay', 3) ''')

con.commit()

name = input("Enter singer's name :")
#name = 'Justin'
rows = cur.execute("select * from album where singer like ?",(name+'%',))

for r in rows :
    print(r)


#for r in rows :
    