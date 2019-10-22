# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:15:24 2019

@author: JC
"""
import numpy as np
arr = np.arange(10)
print(arr) #([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[5])  #第6个元素,从0开始数
print(arr[5:8])  #从第6个元素开始,到第9个元素停止,不包括第9个
arr[5:8] = 12  #对arr[5:8]赋值，使得原数组改变
print(arr)
