# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 12:01:41 2019

@author: JC
内容：使用xlim函数和ylim函数控制x轴和y轴的显示范围
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)#创建x轴上的1000个均匀分布的点
y = np.random.rand(1000)#令每个点的y值为随机数
plt.scatter(x, y, label="散点图")#绘制散点图
plt.xlim(2, 10)  #x轴的显示范围设置为2到10
plt.ylim(0,1)   #y轴的显示范围设置为0到1
plt.legend()#显示图例
plt.show()#显示图片
