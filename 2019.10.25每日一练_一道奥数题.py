# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:26:42 2019

@author: JC
"""
#四个数字h,s,z,y,如果hsh+yzh=yzhs,求这四个数字.
list1=[0,1,2,3,4,5,6,7,8,9]

for h  in list1:

   for s in list1:

       for z in list1:

            for y in list1:

               if (h*100+s*10+h)+(y*100+z*10+h)==(y*1000+z*100+h*10+s):

                   print(h,s,y,z)
