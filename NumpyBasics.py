# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:18:31 2019

@author: Shraddha
"""

import numpy as np
           

# Creating a numpy array

nlist = [5,7,10,8,12,3]
npr = np.array(nlist)
npr = np.array(nlist)
print(npr)

## Multi dimensional array ###
nlist = [[2,3,4], [5,4,2], [6,4,3]]
npm = np.array(nlist)
print(npm)

### arange function - similar to range function in python. Creates nupy array

npv = np.arange(2,12,2)

### creating vector of zeroes
npr = np.zeros(5)
npr = np.zeros((2,3))
npo = np.ones(3)

##linspace - creates equally spaced vaules

npr = np.linspace(3,9)

npr = np.linspace(3,9,12)

## IDENTITY MATRIX #######
npm = np.eye(4)


######## RANDOM NUMBERS ##############

#Generate 5 random number between 0 and 1
np.random.rand(5)       


# more concentrated towards 0 and hence contains negative values
np.random.randn(5)


#generate 6 nos between 3 and 12
np.random.randint(3,12,6)

#to create a matrix
np.random.randint(3,12,(3,2))

#to convert a vector to matrix
npv = np.random.randint(10,50,10)
npm = npv.reshape(5,2)

#max and min
npm.max()
np.max(npm)

npm.min()
np.min(npm)

#### to find index number of min and max locatio in array.
#if multidimensional, it'll convert into 1 dimentsion internally and then give the index

npm.argmax()
npm.argmin()

### to find dimension - or to predict a vector or matrix. Doesnt give shape of matrix
npm.ndim

#to get number of row and columns
npm.shape



nlist = [[90,100,70], [120,70,110], [80,60,30], [130,50,20]]
narr = np.array(nlist)
narr[1][1]
narr[3][0]


##multiple extraction
#multiple extraction to be done in in bracket
#rows and columns separated by comma
narr[:3,:2]
narr[1:,1:]
narr[2:,:2]

narr[:,1:2]
#or
narr[:,1]

[narr[0][0],narr[2][1], narr[3][2]]


### Logical operators
narr > 90

#will fetch values satisfying condition
narr[narr>90]

narr[narr==70]

narr[(narr>80) & (narr<120)]

## == will check for equal dimensins


### broadcasting
narr[:3,:2] = 50

#converting a multidimensional to 1 dimensional

narr.flatten()

#gives the values after flattening
narr.flat[3]

#bin count

np.bincount(narr.flatten()).argmax()

narr+5
narr*2
#Sum
narr.sum()

##summing rows and column
#Axis = 1 - row wise sum
#axis =0 - column wise sum

narr.sum(axis=1)

nlist = [5,8,12,np.nan, 15, np.nan, 22]
npv = np.array(nlist)
npv.sum()

np.nansum(npv)


###### Fancy Indexing  #######

r = [0,1,3]
c = [1,2,1]

narr[r,c]

#slicing will take evry element in the row
narr[:2,c]

########## SORTING ################

np.sort(narr, axis=0)

np.argsort(narr,axis=0)

############ PARTIAL SORTING #############
new = narr.flatten()
np.partition(new,4)

##### STRUCTURED DATA ###############33
#structured data always stored in binary

stdgrade = np.zeros(5, dtype = [('fname', 'a20'),('lname', 'a20'), ('grade', 'f4')])

stdgrade[0] = ('Shraddha', 'Dharmik', 96)
stdgrade[1] = ('Sameer', 'Pophali', 92)

gr = stdgrade['grade']
gr.mean()

stdgrade[stdgrade['grade'] > 85]


#################33 LET's CODE ###############333
'''
1. Find the rows for which the first value (value in position 0) in the row 
is greater than 2
'''
example_list=[[1, 2, 4, 3],[3, 5, 4 ,2],[4, 6, 1, 7],[5, 3, 3, 1],[0, 4, 3, 2], [1 ,9 ,8, 3]]
npm = np.array(example_list)
npm[npm[:,0]>2]

'''
2. Find the rows where the element in position 2 in the row equals 4
'''

npm[npm[:,2]==4]

'''
3.
Create a 5x5 array with random values and find the minimum and maximum values
'''

npr = np.random.randint(1,100,(5,5))
npr.max()
npr.min()

'''
4. Check whether the two arrays are equal
	ar_list1=[3,4,5] ; ar_list2=[3,5,4]
'''
ar_list1=[3,4,5]
ar_list2=[3,5,4]

ar_list1 == ar_list2

'''
5. Create a random 10x4 array and extract the first five rows of the array and 
store them into a variable
'''

npr1 = np.random.randint(0,500, (10,4))
newNpr = npr1[:5,:]

'''
6. Create a random vector of size 10 and sort it in ascending and descending
'''

arrR = np.random.randint(0,100,10)
np.sort(arrR)
np.sort(arrR)[::-1]


'''
7. Find the nearest value from a given value in an array
	example_list = [[12,3,4],[6,7,4],[10,8,11]] & value is 7.8
'''
example_list = [[12,3,4],[6,7,4],[10,8,11]]
npr = np.array(example_list)

index = np.argmin(np.abs(npr - 7.8))
npr.flat[index]


'''
8. Create a random vector of size 15 and replace the maximum value by -1
'''

npm = np.random.randint(1,30,15)
npm[np.argmax(npm)] = -1







