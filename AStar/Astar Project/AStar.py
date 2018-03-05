'''A class for the node needed in Astar.'''
from vector2 import Vector2 
from GraphAndNodeClass import Graph
from GraphAndNodeClass import Node

class Astar:
    def __init__(self,search_space):
        self.search_space = search_space
        self.closed_list = []
        self.open_list = []
        self.goal_node = None
        self.start_node = None

    def sort_open(self):
        #sorts open list by fscore

    def A_star(self,start_Node,goal_Node, search_space):
        self.start_node = start_Node
        self.goal_node = goal_Node
        current = self.start_node        
        #step1 add starting node to the open list.
        self.open_list.append(current)
        #step2 start Loop while open list is not empty.
        while self.open_list:            
            #2a Look for lowest f score in open list.
            self.sort_open()
            current = self.open_list[0]
            # 2b switch the lowest f score to the closed list.
            # 2c Get neighbors.
            # 2d Loop through all neighbors.
                #if non transvisble or in closed list 
                # ignore node
                #otherwise if not in the openlist
                #add to open list then calculate g,h,f, and score
                #if in the open list check path by compareing g scores
                #if in closed list break out of the Loop
              

