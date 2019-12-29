# -*- coding: utf-8 -*-
"""
@author: JC
"""
#axes
import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(4))
print("The axes are:")
print(s.axes)