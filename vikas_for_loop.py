# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:25:22 2020

@author: vikas
"""
#for loop
for i in range(1,10): #range define of i range(min max)
    print("Value of i = "+ str(i)); #counter
print("For loop Complete!!!");

#for loop using . format
for num_1 in range(1,10):
    print("No.{} squared is {} and cubed is {}".format(num_1,num_1**2,num_1**3))
print("For Loop Complete!!!!");

for i in range(20,1,-2): #range define of i range(max min intervel)
    print('i is now {}'.format(i))

#for loop using length of string
num_2 = '7,112,262,025,584,445,607';

for j in range(0,len(num_2)):
    print(num_2[j])

#for loop using if-else
num_3 = '7,112,262,025,584,445,607';
print(type(num_3))
for k in range(0,len(num_3)):
    if num_3[k] in '0123456789': #Comparing given number with 0123456789
        print(num_3[k],end='') #removing new line

#converting string value in integer value
num_4 = '7,112,262,025,584,445,607';
cleanedNumber ='';

for l in range(0,len(num_4)):
    if num_4[l] in '0123456789':
        cleanedNumber = cleanedNumber + num_4[l]
        
newNumber = int(cleanedNumber); #converting string into integer 
print(type(newNumber));
print("The number is {}".format(newNumber));

