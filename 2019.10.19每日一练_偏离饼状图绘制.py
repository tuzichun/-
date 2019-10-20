# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:19:08 2019

@author: JC
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"] = ["SimHei"]#设置中文的字体
mpl.rcParams["axes.unicode_minus"] = False
labels = ["A难度水平", "B难度水平", "C难度水平", "D难度水平"]#设置对应部分的文字说明
students = [0.35, 0.15, 0.20, 0.30]#对应数据
colors = ["#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]#设置对应的颜色
explode = [0.1, 0.1, 0.1, 0.1]#设置饼部分偏离中心的百分比，形成凸出的效果
plt.pie(students,explode=explode,labels=labels,autopct="%3.1f%%",startangle=45,shadow=True,colors=colors)#shadow为设置阴影

plt.title("选择不同难度测试试卷的学生占比")#设置题目
plt.show()