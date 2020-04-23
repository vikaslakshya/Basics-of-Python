# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:08:46 2020

@author: vikas
"""
#string formating
msg_1 = 'Basics of python';
msg_2 = 'by vikas';

message_3 = msg_1+', '+msg_2 +', Are you learning?';
print(message_3);

#string formating using  .format
message_4 = '{}, {}, Are you learning?'.format(msg_1,msg_2);
print(message_4);

#string formating using  f'' function
message_5 = f'{msg_1}, {msg_2}, Are you learning?';
print(message_5);

message_6 = "Basics of Python by vikas, are you learning";
print(message_6);
print(type(message_6));#tells about class of variable
print(message_6.lower());#all letters are converted in lower case
print(message_6.upper());#all letters are converted in upper case
print(message_6.__len__());#length of given string
print(len(message_6));#length of given string
print(message_6.count('e'));#count of any letter in ginen string
print(message_6.find('learning'));#find perticuler word
print(message_6[10]);#print perticuler latter on the basis of their sequence
print(message_6[0:10]);#print perticuler message on the basis of their sequence