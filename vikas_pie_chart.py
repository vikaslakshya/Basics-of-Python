# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:56:29 2020

@author: vikas
"""
import matplotlib.pyplot as plt

activites = ['eat','sleep','work','play']

slices = [3,7,8,6]

colors = ['r','g','m','b']


plt.pie(slices, labels=activites, colors=colors,startangle=90,shadow=True,
       explode=(0.2,0,0,0),autopct='%1.2f%%')

plt.legend()

plt.show()

