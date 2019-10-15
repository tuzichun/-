# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 9:32:40 2019

@author: JC
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05,10,1000)
y = np.sin(x)

plt.plot(x, y, ls="-", lw=2, c="c", label="function") #绘制函数

plt.legend()#显示label

plt.axhline(y = 0.0, c="c", ls="--", lw=2)  #axh轴代表水平，绘制出y值取值为0.0的参考线
plt.axvline(x = 4.0, c="c", ls="--", lw=2)  #axv代表竖直，绘制出x值取值为4.0的参考线

plt.show()