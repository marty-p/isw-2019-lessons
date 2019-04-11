# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:36:00 2019

@author: Studente
"""
import numpy as np
import random
numbers = random.sample(range(50), 20)
numbers_array = np.array(numbers)
arange=np.arange(5,100,3)

# column vector n x 1
numbers_array.shape

# row vector 1 x n
reshaped_numbers = numbers_array.reshape(1,20)

# multidimensional array 2x4
array=np.array([[1,3,5,6],[2,4,7,9]])

#operations between arrays
numbers_2=np.array(random.sample(range(100), 20))

difference = numbers_array - numbers_2
product = numbers_array * numbers_2

#returns a boolean array
print(np.isin(numbers_array, numbers_2))

# returns a boolean array
# check nan presence
array_2 = np.array([np.nan, 2,6,7, np.nan, 10, 8, np.nan])
print(np.isnan(array_2))

# esercizio: sostituire gli np.nan con lo zero
for i,v in enumerate(array_2):
    if np.isnan(v):
        array_2[i] = 0
# not work:
for e in array_2:
    if np.isnan(e):
        e = np.nan
#
