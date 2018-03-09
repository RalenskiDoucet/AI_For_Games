'''A class for the node needed in Astar.'''
from vector2 import Vector2 
from GraphAndNodeClass import Node
from GraphAndNodeClass import Graph
class Astar:
    def __init__(self,search_space):
        self.search_space = search_space
        self.closed_list = []
        self.open_list = []
        self.goal_node = None
        self.start_node = None
    def sort_open_list(self):
        #sorts open list by fscore
        #compare the value in the list to every other putting the smaller value
        for i in range(0,len(self.open_list)):
            for j in range(0,len(self.open_list)):
                #Compare the fscore at index i to fscore at index j
                #if at index j less than index i swap places
                if (self.open_list[i].f_score < self.open_list[j].f_score):
                    temp = self.open_list[i]
                    self.open_list[i] = self.open_list[j]
                    self.open_list[j] = temp

    def A_star(self,start_node,goal_node, search_space):
        self.start_node = start_node
        self.goal_node = goal_node
        current = self.start_node        
        #step1 add starting node to the open list.
        self.open_list.append(current)
        #step2 start Loop while open list is not empty.
        while self.open_list:            
            #2a Look for lowest f score in open list.
            self.sort_open()
            current = self.open_list[0]
            # 2b switch the lowest f score to the closed list.
            self.open_list.remove(current)
            self.closed_list.append(current)
            if self.closed_list.__contains__(self.goal_node):
                return self.draw_path()
            # 2c Get neighbors.
            temp = current.find_neighbors(search_space)
            # 2d Loop through all neighbors.
            for node in temp:                
                #if non transvisble or in closed list
                if not node.is_traversable or self.closed_list.__contains__(node):
                    continue
                #otherwise if not in the openlist
                    if not self.open_list.__contains__(node):
                        self.open_list.append(node)
                #then calculate g,h,f, and score                
                    node.calculate_g_score(current)
                    node.calculate_h_score(goal_node)
                    node.calculate_f_score()
                #add to open list
                 #if in the open list check path by compareing g scores
                #if in closed list break out of the Loop
                    if self.closed_list.__contains__(goal_node):
                        break
            #if goal in closed list return path
    def draw_path(self):
             paths = []
        while self.current_node.parent is not None:
            paths.append(self.current_node)
            self.current_node = self.current_node.parent
        paths.append(self.current_node.parent)
        self.paths = paths
            
            

def main():
    b = Graph(10)
    c = b.nodes[0].find_neighbors()
    a = Astar()  

             
main()
