# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:56:38 2020

@author: vikas
"""
string = "abcdefghij";#string define

for var_1 in string:
    print(var_1);#print string

#print string using iterator
my_iterator = iter(string);
print(my_iterator);#starting location of string
print(next(my_iterator));#value of 1st location of string
print(next(my_iterator));#value of 2nd location of string
print(next(my_iterator));#value of 3rd location of string
print(next(my_iterator));#value of 4th location of string
print(next(my_iterator));#value of 5th location of string
print(next(my_iterator));#value of 6th location of string
print(next(my_iterator));#value of 7th location of string
print(next(my_iterator));#value of 8th location of string
print(next(my_iterator));#value of 9th location of string
print(next(my_iterator));#value of 10th location of string


string = "1234567890";

for var_2 in iter(string):
    print(var_2);


day = ['Mon','Tue','Wed','Thrus','Fri','Sat','Sun'];

week = iter(day);


for char in range(0,len(day)):
    next_iter = next(week);
    print(next_iter);





