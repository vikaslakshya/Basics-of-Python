# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:03:14 2020

@author: vikas
"""
#Dictionaries
dog = {'breed':'papillon','size':'small','color':'white','disposition':'jolly'};
print(dog['breed']);
print(dog['size']);
print(dog['color']);
print(dog['disposition']);


ani_1 =['dog','rabbit','cat'];
ani_2 =['rabbit','cat','dog'];
print(ani_1 == ani_2);



ani_1 = {'breed':'papillon','size':'small','color':'white','disposition':'jolly'};
ani_2 = {'color':'white','disposition':'jolly','size':'small','breed':'papillon'};
print(ani_1 == ani_2);


person = {'name':'vikas','gender':'M','age':'33'};

for i in person.values():
    print(i);


for j in person.keys():
    print(j);


for k in person.items():
    print(k);


birthdays = {'akash':'Oct 22','vishnu':'Aprl 10','vikas':'Jul 20'};

while True:
    print("Enter the name : ");
    name = input();
    if name =='':
        break;
        
    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+ name);
        
    else:
        print('I do not have birthday info for '+ name);
        
        print('What is their birthday?');
        bday = input();
        birthdays[name] = bday;
        print('Birthday database is updated');

