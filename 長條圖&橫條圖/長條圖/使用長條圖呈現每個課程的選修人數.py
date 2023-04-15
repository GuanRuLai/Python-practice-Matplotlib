# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 19:06:06 2023

@author: HP
"""

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
fontManager.addfont("TaipeiSansTCBeta-Regular.ttf")
matplotlib.rc("font",family="Taipei Sans TC Beta")

listx=["c","c++","c#","java","python"]
listy=[45,28,38,32,50]
plt.bar(listx,listy,width=0.5,color=["r","g","b"])
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")
plt.show()
