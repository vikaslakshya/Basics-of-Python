# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:55:31 2020

@author: vikas
"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]

y = [2,4,5,7,6,8,9,10,12,11]

plt.scatter(x,y,label="Stars",color='red',marker = "*",s=30)

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('Scatter Plot')

plt.legend()

plt.show()

