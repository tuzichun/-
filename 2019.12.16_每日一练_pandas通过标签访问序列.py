"""
@author: JC
"""
#通过标签访问序列
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s['a'])