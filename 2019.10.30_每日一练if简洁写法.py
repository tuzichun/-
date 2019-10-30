# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:01:59 2019

@author: JC
"""
#普通写法
a, b, c = 1, 2, 3
if a>b:

    c = a

else:

    c = b
    
#简洁写法
c = a if a>b else b