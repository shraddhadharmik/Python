# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:02:14 2019

@author: Shraddha
"""

import sqlite3
import csv


csvdata = csv.reader(open('student.csv'))
con = sqlite3.connect('student.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS student')

cur.execute('''create table student(
            id int,
            name text,
            course text,
            spec text,
            grade int            
            )''')

for c in csvdata :
    cur.execute('insert into student values(?,?,?,?,?)',(c[0],c[1],c[2],c[3],c[4]))
    
con.commit()
rows = cur.execute('select * from student')
for r in rows :
    print(r)
con.close()
    