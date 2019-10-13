# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 22:03:18 2019

@author: JC
"""

import matplotlib.pyplot as plt #导入绘图库
import numpy as np #导入numpy


x = np.linspace(0.05, 10, 2000) #取2000个点
y = np.cos(x) #对应的y值,使用cos函数
plt.plot(x,y,ls="-", lw=2, label="plot figure")#绘图
'''
ls-------->线条的风格
lw--------->线条的宽度
label-------->标记图形内容的标签文本
'''