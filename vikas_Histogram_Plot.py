# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:53:45 2020

@author: vikas
"""


import matplotlib.pyplot as plt

age = [6,10,12,24,26,28,3,43,34,35,37,29,27,22,33,55,44,66,56,47,38,26,];

range = (0,100);
dist = 10;

plt.hist(age,dist,range,color='red',histtype='bar',rwidth=0.5);

plt.xlabel('Age');
plt.ylabel('Distribution');

plt.title('Histogram Plot');

plt.show();
