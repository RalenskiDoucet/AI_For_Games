'''A class for the node needed in Astar.'''
from vector2.py import vector2 
class Node(object):
    def __init__(self, position):
        self.postion = position
        self.is_transversible = False
        self.parent_node = None
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
    def find_neighbors(self,position):
        '''Loop through all the nodes in the graph'''
        '''Compare each of the nodes position to see if it's position is a valid neighbor position'''
        '''add to neighbor list'''
        valid_positions = [] 
        valid_positions.append (top_neighbor = current + <0, 1>
        valid_positions.append (bottom_neigbor = current + <0, -1>)
        valid_positions.append (left_neighbor = current + <-1, 0>)
        valid_positions.append (right_neighbor = current + <1, 0>)
    def calculate_gscore(self, g_score):
        '''Loop through the graph to find current node's position'''
        '''Find movement cost'''
        '''Add current node to movement cost'''
        movement_cost=10
        current_node=raw_input("")
        goal_node=raw_input("")
        g_score=movement_cost+current_node
        print g_score
    def calcuate_hscore(self,postion,g_score):
        '''Loop through graph find the number of nodes between current and goal then number of nodes times 10.'''

