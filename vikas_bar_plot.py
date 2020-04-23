# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:51:15 2020

@author: vikas
"""
import matplotlib.pyplot as plt #call matplot library
#corona cases in state wise
x = [1,2,3,4,5]; #defining x-axis

y = [52.21,22.72,21.56,18.01,15.96]; #defining y-axis

tick_label = ['MH','GJ','DL','RJ','TN']; #label bar
#calling bar function
plt.bar(x,y,tick_label=tick_label,width = 0.7,color=['red','blue','blue','green','green',]);

plt.xlabel('State'); #x-axis labeling

plt.ylabel('Corona Cases in K'); #y-axis labeling

plt.title('Corona Cases state wise'); #titling of plot

plt.show(); #showing plot

