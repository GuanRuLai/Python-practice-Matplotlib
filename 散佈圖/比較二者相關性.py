# -*- coding: utf-8 -*-
"""
Created on Wed May  3 21:38:32 2023

@author: HP
"""

import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8]
y=[1,4,9,16,7,15,17,19]
sizes=[20,200,100,50,500,1000,60,90]
colors=["red","green","black","orange","purple","pink","cyan","magenta"]
plt.scatter(x,y,s=sizes,c=colors)
plt.show()
