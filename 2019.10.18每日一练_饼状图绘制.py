# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:31:10 2019

@author: JC
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"] = ["SimHei"]#设置中文字体
mpl.rcParams["axes.unicode_minus"] = False
labels = ["A难度水平", "B难度水平", "C难度水平", "D难度水平"]#文字说明
students = [0.35, 0.15, 0.20, 0.30]#数据导入
colors = ["#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]#颜色设置
explode = [0.1, 0.1, 0.1, 0.1]#偏离程度
plt.pie(students, labels=labels, autopct="%3.1f%%", startangle=45, pctdistance=0.7, labeldistance=1.2, colors=colors)#饼状图绘制

plt.title("选择不同难度测试试卷的学生占比")
plt.show()