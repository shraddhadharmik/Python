# -*- coding: utf-8 -*-
"""
Created on Mon May 27 10:11:49 2019

@author: Shraddha
"""


import xml.etree.ElementTree as et

data = '''
<person> 
<name>Chuck</name> 
<phone type="intl"> +1 734 303 4456 </phone>
 <email hide="yes"/>
 </person>
'''

#string is converted into xml tag
info = et.fromstring(data)


#find = to get the value inside tags
#get =  to get the assigned value
print('Name : ', info.find('name').text)
print('Phone : ', info.find('phone').get('type'), info.find('phone').text)
print('Email : ', info.find('email').get('hide'), info.find('email').text)



input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''

data = et.fromstring(input)
info = data.findall('users/user')

for i in info :
    print('X : ', i.get('x'))
    print('ID : ', i.find('id').text)
    print('Name : ', i.find('name').text)


######HOMEWORK QUESTION ################
    
import requests
import bs4
url = 'https://www.imdb.com/list/ls021116007/'
inputString = requests.get(url)
soup = bs4.BeautifulSoup(inputString.text, 'html.parser')

lst = soup.findAll('h3.lister-item-header')
genre = soup.findAll('span', {'class' : 'genre'})
rating = soup.findAll('span', {'class' : 'ipl-ratinsg-star__rating'})

