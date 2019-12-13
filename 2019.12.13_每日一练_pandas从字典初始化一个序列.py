# -*- coding: utf-8 -*-
"""
@author: JC
"""
#从字典初始化一个序列
import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)
