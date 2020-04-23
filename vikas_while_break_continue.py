# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:15:41 2020

@author: vikas
"""
#While loop by using break loop
name = 'vikas';

while True:
    print("Please enter your name : ");
    name1 = input(); #taking input
    if name1 == name: #comparing
        break; #break loop
print('Thank You',name);

#While loop by using continue loop
while True:
    print('Who are you?');
    name = input();
    
    if name != 'vikas':
        continue;
        
    print("Hello, vikas. what is your password'It is a dog'");
    password = input();
    if password == 'pug':
        break;
print('Congrats!!!, Access Granted');

