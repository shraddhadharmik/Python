# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:27:58 2019

@author: Shraddha
"""

import matplotlib.pyplot as plt

values = [1,5,8,9,2,0,3,10,4,7]


plt.plot(range(0,10), values)   #line graph
plt.show()

#plotting single line
plt.plot(range(0,10), values, '--yo')   #line graph
plt.show()


#plotting multiple lines
values2 = [3,8,12,11,8,7,5,7,4,2]
plt.plot(range(0,10), values, '--yo')
plt.plot(range(0,10), values2, '--r*')
plt.title('2 Line Graph')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
#loc is location where you want the legend
plt.legend(['1st line', '2nd line'], loc=4)

#to send subdivision in plotting
ax = plt.axes()
ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
ax.set_yticks([2,4,6,8,10,12,14,16])

#for grid to appear
plt.grid()

#for anotation to appear - any point to be highlighted as highest,lowest etc
plt.annotate(xy = [8,4], s='Similar product')
plt.savefig('2linegraph.jpg')
plt.show()



#############PIE CHART###############33
values=[5,8,9,10,4,7]
col = ['b','g','r','y', 'm', 'c']
lab = ['A', 'B', 'C', 'D', 'E', 'F']
exp = [0,0,0,0.2,0,0]
#autopct for percentage
#counterclock for display of labels in clockwise or counterclockwise direction
plt.pie(values, colors=col, labels = lab, explode=exp, shadow = True, autopct = '%1.1f%%', counterclock = True)
plt.show()



######################BAR CHART ##########################3
yvalues=[5,8,9,10,4,7]
xvalues=range(1,7)
col = ['b','g','r','y', 'm', 'c']
plt.bar(xvalues, yvalues, color = col)

for x,y in zip(xvalues, yvalues) :
    plt.text(x,y,y)
plt.show()


### Example 2 ###
city=['Delhi','Beijing','Washington','Tokyo','Moscow']
happiness_index=[60,40,70,65,85]
col = ['b','g','r','y', 'c']
plt.bar(city, happiness_index, color = col)
for x,y in zip(city, happiness_index) :
    plt.text(x,y,y)
plt.xlabel('City')
plt.ylabel('Happiness Index')
plt.title('Graph showing city v/s hapiness index')
plt.show()

################# HISTOGRAM #####################33
values = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
plt.hist(values, 10, edgecolor = 'k', color='g')
plt.show()

heights=[189 ,170, 189, 163, 183, 171, 185, 172, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173,  174, 183, 183, 168, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183,  177, 185, 188, 188, 182, 185]
plt.hist(heights, 8, edgecolor = 'b', color='y')
plt.show()


########################## BOX PLOT ############################
value1 = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
value2 = [62,5,91,25,36,32,96,95,3,90,95,32,27,55,100,15,71,11,37,21]
value3 = [23,89,12,78,72,89,25,69,68,86,19,49,15,16,16,75,65,31,25,52]
value4 = [59,73,70,16,81,61,88,98,10,87,29,72,16,23,72,88,78,99,75,30]
lab = ['Course 1', 'Course 2', 'Course 3', 'Course 4']

boxdata = [value1, value2, value3, value4]
#patch_artist used to fill color
#vert = 0 will give a horizontal box plot
plt.boxplot(boxdata, patch_artist = True, labels=lab, vert = 0)
plt.show()


###################### SCATTER PLOT ##########################3

weight1=[63.3,57,64.3,63,71,61.8,62.9,65.6,64.8,63.1,68.3,69.7,65.4,66.3,60.7]
height1=[156.3,100.7,114.8,156.3,237.1,123.9,151.8,164.7,105.4,136.1,175.2,137.4,164.2,151,124.3]

plt.scatter(weight1, height1, c='r', marker = '*')
plt.show()

### Example 2
weight1=[57,58.2,58.6,59.6,59.8,60.2,60.5,60.6,60.7,61.3,61.3,61.4,61.8,61.9,62.3]
height1=[100.7,195.6,94.3,127.1,111.7,159.7,135,149.9,124.3,112.9,176.7,110.2,123.9,161.9,107.8]
 
weight2=[62.9,63,63.1,63.2,63.3,63.4,63.4,63.4,63.5,63.6,63.7,64.1,64.3,64.3,64.7,64.8,65]
height2=[151.8,156.3,136.1,124.2,156.3,130,181.2,255.9,163.1,123.1,119.5,179.9,114.8,174.1,108.8,105.4,141.4]
 
weight3=[69.2,69.2,69.4,69.7,70,70.3,70.8,71,71.1,71.7,71.9,72.4,73,73.1,76.2]
height3=[166.8,172.9,193.8,137.4,162.4,137.1,169.1,237.1,189.1,179.3,174.8,213.3,198,191.1,220.6]

#s mentions the size
plt.scatter(weight1,height1, c='r', marker='*', s=50)
plt.scatter(weight2,height2, c='g', marker='_', s=70)
plt.scatter(weight3,height3, c='c', marker='+', s=90)

#to get the figure size and set it to cusomtized values
fig = plt.rcParams['figure.figsize']
print(fig[0], fig[1])
fig[0] = 6
fig[1] = 4
plt.rcParams['figure.figsize'] = fig
plt.show()

############# CORRELATION MATRIX ############33
import numpy as np
cor = np.polyfit(weight1,height1, 1)
p = np.poly1d(cor)
plt.plot(weight1, p(weight1), 'm')
plt.show()

##### let's code ###
#1.
import random

plt.scatter(random.sample(range(0,100), 10), range(0,10))
plt.title('Graph using Random values')
plt.show()


##2
'''
Write a Python programming to display a bar chart of the popularity of programming Languages. 
Programming languages: Java, Python, PHP, JavaScript, C#, C++
 Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
 '''
 
prog_lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
pop = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

#display values at top
for x,y in zip(prog_lang,pop) :
    plt.text(x,y,y)

plt.bar(prog_lang, pop)
plt.show()

##3
'''
Write a Python programming to create a pie chart of gold medal achievements of five 
most successful countries in 2018 Winter Olympics
Norway – 14; Germany – 15, Canada – 11, United States – 9, Netherlands - 8

'''

countries = ['Norway', 'Germany', 'Canada', 'United States', 'Netherlands']
medals = [14, 15, 11, 9, 8]
col = ['b','r','c','y','g']

plt.pie(medals, labels=countries, autopct='%1.1f%%', colors=col)
plt.show()
 

##4.
'''
Write a Python program to draw a scatter plot comparing two subject marks of Mathematics 
and Science. Use marks of 10 students
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
'''
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


plt.scatter(science_marks, marks_range, c = 'r', marker='*')
plt.scatter(math_marks, marks_range, c = 'c', marker='o')
plt.show()



 
