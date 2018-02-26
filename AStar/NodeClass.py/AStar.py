'''A class for the node needed in Astar.'''
from vector2 import Vector2 
from Grid import Graph
class Node(object):
    def __init__(self, position):
        self.postion = position
        self.is_transversible = False
        self.parent_node = None
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
    def find_neighbors(self,Node,Graph):
        '''Loop through all the nodes in the graph'''
        '''Compare each of the nodes position to see if it's position is a valid neighbor position'''
        '''add to neighbor list'''
        graph=[10]
        current.Node = 5
        
    def calculate_gscore(self,Node):
        '''Determine if new current node is vertical, horzontal, or diagnaol.'''
        if ((self.postion.xpos == Node.position.xpos and self.postion.ypos != Node.position.ypos) or
            (self.postion.xpos != Node.position.xpos and self.postion.ypos == Node.position.ypos)):
            self.g_score = Node.g_score + 10
        else:
            self.g_score = Node.g_score + 14
        '''g_score =g_score + movement_cost'''
        '''Add the new current node movement cost.'''
    
        '''Do to all transversible nodes.'''
    def calcuate_hscore(self,postion,g_score):
        '''Loop through graph find the number of nodes between current and goal then number of nodes times 10.'''

    