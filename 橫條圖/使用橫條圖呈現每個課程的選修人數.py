# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 19:45:17 2023

@author: HP
"""
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
fontManager.addfont("TaipeiSansTCBeta-Regular.ttf")
matplotlib.rc("font",family="Taipei Sans TC Beta")

listy=["c","c++","c#","java","python"]
listx=[45,28,38,32,50]
plt.barh(listy,listx,height=0.5,color=["r","g","b"])
plt.title("資訊程式課程選修人數")
plt.ylabel("程式課程")
plt.xlabel("選修人數")
plt.show()
