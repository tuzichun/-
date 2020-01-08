# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 08:23:12 2020

@author: JC
"""

import networkx as nx #该库用于网络图的创建与绘制
import matplotlib.pyplot as plt

G = nx.cycle_graph(24)
pos = nx.spring_layout(G, iterations=200)
nx.draw(G, pos, node_color=range(24), node_size=800, cmap=plt.cm.Blues)
plt.show()