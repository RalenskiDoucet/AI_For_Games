import pygame
from NodeVisual import NodeVisual
from GraphAndNodeClass import Node
from GraphAndNodeClass import Graph
from vector2 import Vector2
from A_Star import Astar
#A class for the graphs visuals.

class Graph_Visuals(object):
    def __init__(self,Astar_graph,draw_surface,node_offset):
        self.node_offset = Vector2(0,0)#allows us to space the nodes form each other .
        self.draw_surface = draw_surface # the pygame is the surface that we are drawing on.
        self.node_visual = []# A list of visual nodes.
        self.Astar_graph = Astar_graph
            
    def draw_nodes_to_surface(self):
        count = 0 
        for x in range(0,self.Astar_graph * self.node_offset, self.node_offset ):
            for y in range ( 0, self.Astar_graph * self.node_offset, self.node_offset):
                count ++
    def get_visuals(self, NodeVisual):
        for x in range(0,self.Astar_graph)
        return NodeVisual