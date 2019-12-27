# -*- coding: utf-8 -*-
"""
@author: JC
"""
#面板(Panel)是3D容器的数据。
#从序列的字典创建面板
import pandas as pd
import numpy as np


data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)
