# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:30:02 2019

@author: JC
"""

import numpy as np
arr = np.arange(15).reshape(3, 5)#建立顺序序列向量后处理为3×5的矩阵
print(arr)  #输出原始矩阵
print(arr.T)   #转置矩阵的第一种方法
print(np.transpose(arr))#转置矩阵的第二种方法