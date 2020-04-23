# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:39:40 2020

@author: vikas
"""
#plotting Sin Function
import numpy as np #call numpy library
import matplotlib.pyplot as plt #call matplot library

t = np.arange(0.0,2.0,0.02); #defining x-axis(start,end,intervel)

s = 1 + np.sin(2*np.pi*t); #defining y-axis call sin function

plt.plot(t,s,'--'); #call plot (x-axis,y-axis,formate/colour of plot)

plt.grid(); #plot with grid
plt.xlabel('Time(t)'); #x-axis labeling
plt.ylabel('Voltage(mV)'); #y-axis labeling
plt.title('Sine wave plot(Sin(x))'); #titling of plot

plt.show(); #showing plot

