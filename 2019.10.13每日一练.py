# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:14:19 2019

@author: JC
内容：使用scatter绘制散点图
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)#创建x轴上的1000个均匀分布的点
y = np.random.rand(1000)#令每个点的y值为随机数
plt.scatter(x, y, label="散点图")#绘制散点图6
plt.legend()#显示图例
plt.show()#显示图片