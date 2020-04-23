# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:44:47 2020

@author: vikas
"""
#list function
print([1,2,3,4,5,6]);#list of number

print(['cat','dog','rat','elephant']);#list of string


print(['hello','3.14',True,None,42]);#mixed list


animals = ['cat','bat','rat','elephant','dog'];
print(animals);


print(animals[0:7]);#print slicing


print(animals[0]);#print perticular element


print(animals[1]);

print('Barking '+animals[4]);


animals = ['cat','bat','rat','elephant','dog'];
print(animals);


print(animals[-2]);#count from the last


print(animals[:]);#print all element
print(animals[:3]);#print from start and end upto 4th element 
print(animals[1:]);#print from 2nd and end upto last element
print(len(animals));#print length of list

var_1=[[1,2,3,4,5],['cat', 'bat', 'rat', 'elephant', 'dog']];
print(var_1[1][3]);#print 4th element of first list


ani_1=['cat','dog','rat'];
ani_1.append('elephant');#adding element in the list
print(ani_1);

ani_1.insert(1,'chicken');#adding element in perticular position in the list
print(ani_1);

ani_1.remove('chicken');#removing element in the list
print(ani_1);

num_1=[2,5,3.14,-1,-7];
num_1.sort();#shorting element in list
print(num_1);

