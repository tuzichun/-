# -*- coding: utf-8 -*-
"""
@author: JC
"""
#面板(Panel)是3D容器的数据。
#创建面板
import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
p = pd.Panel(data)
print(p)