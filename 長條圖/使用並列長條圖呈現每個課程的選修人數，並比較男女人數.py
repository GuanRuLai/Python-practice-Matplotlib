# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 20:03:20 2023

@author: HP
"""

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
fontManager.addfont("TaipeiSansTCBeta-Regular.ttf")
matplotlib.rc("font",family="Taipei Sans TC Beta")

# 先設定每個項目的寬度（再由子項目分）
width=0.25 
listx=["c","c++","c#","java","python"]
# 使用「串列綜合表達式」之函式將子項目「男」串列中的值逐一向左移動
listx1=[x-width/2 for x in range(len(listx))]
# 使用「串列綜合表達式」之函式將子項目「女」串列中的值逐一向右移動
listx2=[x+width/2 for x in range(len(listx))]
listy1=[25,20,20,16,28]
listy2=[20,8,18,16,22]
plt.bar(listx1,listy1,width,label="男")
plt.bar(listx2,listy2,width,label="女")
plt.xticks(range(len(listx)),labels=listx)
plt.legend()
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")
plt.show()
