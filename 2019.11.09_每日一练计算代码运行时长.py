# -*- coding: utf-8 -*-
"""
Created on Sat Nov 9 21:22:35 2019

@author: JC
"""

import time

start = time.perf_counter()

l = []
for i in range(10000000):
    l.append(i)
    
end = time.perf_counter()

print("执行时长:",end-start,"秒")