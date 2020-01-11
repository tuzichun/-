# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 23:05:03 2020

@author: JC
"""

from random import randint

print('\n'.join([''.join([('TUZICHUN'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
