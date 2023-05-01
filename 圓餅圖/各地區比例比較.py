# -*- coding: utf-8 -*-
"""
Created on Mon May  1 22:28:47 2023

@author: HP
"""

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
fontManager.addfont("TaipeiSansTCBeta-Regular.ttf")
matplotlib.rc("font",family="Taipei Sans TC Beta")

sizes=[25,30,15,10]
labels=["北部","西部","南部","東部"]
colors=["red","green","blue","yellow"]
explode=(0,0,0.2,0) # 第三部分會凸出
plt.pie(sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    labeldistance=1.1,
    autopct="%2.1f%%",
    pctdistance=0.6,
    shadow=True,
    startangle=90)
plt.show()
