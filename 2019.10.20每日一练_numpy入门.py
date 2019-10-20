# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:12:52 2019

@author: JC
"""

import numpy as np


data1 = [[1, 2, 3, 4, 5], [2, 2, 2, 2, 2]]# 生成list
arr1 = np.array(data1)#将list转化为数组格式

print("数组的形状为：",arr1.shape)
print("数组的数据类型为：", arr1.dtype)
print("数组的维度为：", arr1.ndim)



print("输出一个长度为10的顺序向量：\n",np.arange(10))
print("输出一个3×3的零矩阵：\n",np.zeros((3, 3)))
print("输出一个形状和arr1一样的都是1的数组：\n",np.ones_like(arr1))
print("输出一个10维的单位矩阵：\n",np.eye(10))