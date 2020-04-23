# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:30:41 2020

@author: vikas
"""
#Functions 

def function1():
    print("Hello, Basics of python");
    
function1()

#1. No Argu No Return Type
def add():
    num_1 = int(input("Enter the value of num1 : ="));
    num_2 = int(input("Enter the value of num2 : ="));
    
    num_3 = num_1 + num_2;
    
    print("Sum = ",num_3);
    
add();


#2. With Argument and No Retyrn Type
def sub(num_1, num_2):
    num_3 = num_1 - num_2;
    
    print("Sub = ",num_3);
    
sub(10,5);


#3. No Argument and with return type
def multiply():
    num_1 = int(input("Enter the value of num1 : ="));
    num_2 = int(input("Enter the value of num2 : ="));
    
    num_3 = num_1 * num_2;
    
    return num_3;

num_4 = multiply();
print("Multiply = ",num_4);

#4. with Argument and with return type
def div(num_1, num_2):
    
    num_3 = num_1/num_2;
    
    return num_3;

num_4 =  div(49,9);
print("Division = ",num_4);

