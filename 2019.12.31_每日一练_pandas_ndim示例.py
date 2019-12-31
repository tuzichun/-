# -*- coding: utf-8 -*-
"""
@author: JC
"""
#ndim,对象的维数
import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(4))
print(s)

print("The dimensions of the object:")
print(s.ndim)
