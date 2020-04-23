# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:38:12 2020

@author: vikas
"""
var_1 = 0; #variable defining

while var_1<=10: #condition
    print("Value of var1 is",var_1);
    var_1 += 1; #counter


avaiable_exits = ["east","north east","south"];

choosen_exit ="";

while choosen_exit not in avaiable_exits:
    choosen_exit = input("Please enter the direction : ");
    if choosen_exit == "quit":
        print("Your GAME OVER");
        break;
    
else:
    print("Are you not glad that you are out of this loop");

