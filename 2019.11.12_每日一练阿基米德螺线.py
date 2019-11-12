# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:38:22 2019

@author: JC
"""

import numpy as np
from matplotlib import pyplot as plt
t = np.linspace(0, 2 * np.pi, 1001)  # 1001个点，1000等分
r_spiral = 0.8 * t  # 阿基米德螺旋线
plt.figure('Polar', facecolor='lightgray')
plt.gca(projection='polar')  # 设置极坐标系
plt.title('Polar', fontsize=20)
plt.xlabel(r'$\theta$', fontsize=14)
plt.ylabel(r'$\rho$', fontsize=14)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
# 函数值   = f (自变量)
# 垂直坐标 = f (水平坐标)
# 极径     = f (极角)
plt.plot(t, r_spiral, c='dodgerblue',
        label=r'$\rho=0.8\theta$')

plt.legend()
plt.show()