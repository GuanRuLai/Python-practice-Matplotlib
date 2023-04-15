# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 19:54:22 2023

@author: HP
"""

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
fontManager.addfont("TaipeiSansTCBeta-Regular.ttf")
matplotlib.rc("font",family="Taipei Sans TC Beta")

listx=["c","c++","c#","java","python"]
listy1=[25,20,20,16,28]
listy2=[20,8,18,16,22]
plt.bar(listx,listy1,width=0.5,label="男")
plt.bar(listx,listy2,width=0.5,bottom=listy1,label="女")
plt.legend()
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")
plt.show()
