"""
@author: JC
"""
#访问序列
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#输出第一个元素
print(s[0])