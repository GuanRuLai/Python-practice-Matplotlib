# -*- coding: utf-8 -*-
"""
Created on Wed May  3 21:16:48 2023

@author: HP
"""

import matplotlib.pyplot as plt

data=[3,4,2,3,4,5,4,7,8,5,4,6,2,0,1,9,7,6,6,5,4]
plt.hist(data,bins=10)
plt.xlabel("Value")
plt.ylabel("Counts")
plt.grid(True) # 設定格線
plt.show()
