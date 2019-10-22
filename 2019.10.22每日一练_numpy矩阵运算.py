# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:41:56 2019

@author: JC
"""

import numpy as np
data1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
narr1 = np.array(data1)#初始化一个矩阵
print(narr1*narr1)#对应位置元素的乘法运算

print(narr1-narr1)#减法运算

print(1/narr1)#除法运算

print(narr1**2)#开方运算
