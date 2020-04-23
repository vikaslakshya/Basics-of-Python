# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:21:23 2020

@author: vikas
"""
import numpy as np #call numpy library

num_1 = [1,2,3,4]; #defining list

print(type(np.array(num_1))); #converting list into array

arr_1 = np.array(num_1); # n-dimentional array

print(arr_1);


print(np.arange(0,11,2)); #arrange array start from 0 end with 10 with intervel 2


print(np.zeros(5)); #generating zeros matrix of 5x5
print(np.zeros((3,5))); #generating zeros matrix of 3x5


print(np.ones(5)); #generating zeros matrix of 5x5
print(np.ones((3,5))); #generating zeros matrix of 3x5


print(np.random.randint(0,10)); #generating random number from 0 to 10

print(np.random.randint(0,1000,(4,4))); #generating matrix of 4x4 of random number


print(np.random.seed(101)); #seed function using for fixing random values

arr_2 =np.random.randint(0,100,10);

print(arr_2);

print(arr_2.max()); #calculating maximum
print(arr_2.min()); #calculating minimum
print(arr_2.mean()); #calculating mean
print(arr_2.argmax()); #showing index value of maximum number
print(arr_2.argmin()); #showing index value of minimum number
print(arr_2.reshape(2,5)); #reshaping the matrix


#defining array  from 0 to 100 and reshaping into 10x10 matrix
mat = np.arange(0,100).reshape(10,10); 
print(mat);

print(mat[2,2]); #locate perticular value in matrix by using rows and coloum
print(mat[0,:]); #row
print(mat[:,0]); #coloum
print(mat[0:3,0:3]);#print rows and coloum with given range

