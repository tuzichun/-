# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:30:09 2020

@author: JC
"""

import networkx as nx #该库用于网络图的创建与绘制
import matplotlib.pyplot as plt

G = nx.Graph()#创建无向图
G.add_node(1)#加入节点
G.add_edge(2, 3)#加入边
# G.add_edge(3, 2)
print("输出全部节点：{}".format(G.nodes()))
print("输出全部边：{}".format(G.edges()))
print("输出全部边的数量：{}".format(G.number_of_edges()))
nx.draw(G)
plt.show()