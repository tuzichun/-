# -*- coding: utf-8 -*-
"""
@author: JC
"""
#从数组初始化一个序列
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)