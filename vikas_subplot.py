# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:48:25 2020

@author: vikas
"""
import numpy as np #call numpy library
import matplotlib.pyplot as plt #call matplot library

x1 = np.linspace(0.0,5.0); #defining x-axis with line spaceing
x2 = np.linspace(0.0,2.0); #defining x-axis with line spaceing

y1 = np.cos(2*np.pi*x1)*np.exp(-x1); #defining y-axis by using cos function
y2 = np.cos(2*np.pi*x2); #defining y-axis by using cos function

plt.subplot(2,1,1); #using sub plot(row,coloum,position)
plt.plot(x1,y1,'o-'); #call plot (x-axis,y-axis,formate/colour of plot)
plt.title('Subplot-1'); #titling of plot
plt.xlabel('x1'); #x-axis labeling
plt.ylabel('Amp(y1)'); #y-axis labeling

plt.subplot(2,1,2); #using sub plot(row,coloum,position)
plt.plot(x2,y2,'.-'); #call plot (x-axis,y-axis,formate/colour of plot)
plt.title('Subplot-2'); #titling of plot
plt.xlabel('x2'); #x-axis labeling
plt.ylabel('Amp(y2)'); #y-axis labeling

plt.show(); #showing plot


