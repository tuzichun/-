# -*- coding: utf-8 -*-
"""
@author: JC
"""
#empty
import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(4))
print("Is the Object empty?")
print(s.empty)
