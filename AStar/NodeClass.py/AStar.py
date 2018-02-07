 '''A class for the node needed in Astar.'''
class Node(object)
    def __init__(self, position):
        self.postion = postion
        self.is_transversible = False
        self.parent_node = None
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
    def find_neighbors(self,position):
