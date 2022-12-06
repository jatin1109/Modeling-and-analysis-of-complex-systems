import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import networkx as nx
import random as rd

p_i = 0.04 # infection probability
p_r = 0.5 # recovery probability
p_e = 0.05 # edge probability
n = 200 #number of edges

def initialize():
    global g
    g = nx.erdos_renyi_graph(n, p_e)
    g.pos = nx.spring_layout(g)
    for i in g.nodes:
        g.nodes[i]['state'] = 1 if random() < .5 else 0

def observe():
    global g
    cla()
    nx.draw(g, vmin = 0, vmax = 1,
            node_color = [g.nodes[i]['state'] for i in g.nodes],
            pos = g.pos)

def update():
    global g
    for a in list(g.nodes):
        if g.nodes[a]['state'] == 0: # if susceptible
            for b in list(g.neighbors(a)):
                if g.nodes[b]['state'] == 1: # if neighbor b is infected
                    if random() < p_i:
                        g.nodes[a]['state'] = 1
                        break
                    else:
                        g.nodes[a]['state'] = 0
        else: # if infected
            g.nodes[a]['state'] = 0 if random() < p_r else 1

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])