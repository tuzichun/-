# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:17:24 2019

@author: JC
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05,10,1000)
y = np.sin(x)

plt.plot(x, y, ls="-.", lw=2, c="c",label = "flot figure") #设置图例对应的文字为“flot figure”

plt.legend(loc="upper right")#flot figure的位置，upper，left，right，lower等组合而成

plt.show()
