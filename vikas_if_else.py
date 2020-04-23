# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:58:18 2020

@author: vikas
"""
name = input("Please enter your name : ")
age = int(input("What is your age, {0}? ".format(name)))

print(age)


if age >=18:
    print("You can give vote!!!")
    
else:
    print("You can give vote after {0} year.".format(18-age))


print("Please guess a number b/w 1 to 10")
guess = int(input())

if guess < 5:
    print("Please guess higher")
    
    guess = int(input())
    if guess == 5:
        print("Well done, your guess is correct!!")
    else:
        print("Sorry, you have not not guessed the correct number")
elif guess > 5:
    print("Please guess lower")
    
    guess = int(input())
    if guess == 5:
        print("Well done, your guess is correct!!")
    else:
        print("Sorry, you have not not guessed the correct number")
else:
    print("You got it first time")

