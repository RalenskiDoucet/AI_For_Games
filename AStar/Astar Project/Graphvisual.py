import pygame
from NodeVisual import NodeVisual
from GraphAndNodeClass import Node
from GraphAndNodeClass import Graph
from vector2 import Vector2
from A_Star import Astar

class Graph_Visuals(object):
'''A class for the graphs visuals.'''    
    def __init__(self,Astar_graph,draw_surface,node_offset):
        self.node_offset = Vector2(0,0)#allows us to space the nodes form each other .
        self.draw_surface = draw_surface # the pygame is the surface that we are drawing on.
        self.node_visual = []# A list of visual nodes.
        self.Astar_graph = Astar_graph
            
    def draw_nodes_to_surface(self,Node,Graph):
'''A Function to get the nodes to show in the pygame window.'''
        count = 0 
        for x in range(0, self.graph.dims * self.node_offset, self.node_offset): 
            for y in range(0, self.graph.dims * self.node_offset, self.node_offset):
             node = NodeVisual(self.graph[count], Vector2(x, y), [0,0], self.draw_surface) 
                if not Node.node.traversable:
    
    def get_visuals(self, NodeVisual):
 '''A fuction that fetches all the visuals from the NodeVisual class.'''
        for x in range(0,self.Astar_graph)
        return NodeVisual
    
    def update(self,events):
        for Node in self.node_visual:
            Node.update(events)
            if NodeVisual.is_hoovered:
                self.selected_node


