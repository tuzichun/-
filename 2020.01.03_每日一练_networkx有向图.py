# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 12:41:21 2020

@author: JC
"""

import networkx as nx #该库用于网络图的创建与绘制
import matplotlib.pyplot as plt

G = nx.DiGraph()#创建有向图
G.add_node(1)
G.add_node(2)
G.add_nodes_from([3, 4, 5, 6])
G.add_cycle([1, 2, 3, 4])
G.add_edge(1, 3)
G.add_edges_from([(3, 5), (3, 6), (6, 7)])
print("输出全部节点：{}".format(G.nodes()))
print("输出全部边：{}".format(G.edges()))
print("输出全部边的数量：{}".format(G.number_of_edges()))
nx.draw(G)
plt.show()