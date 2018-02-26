'''A class that generates a graph and nodes in the graph.'''
from AStar import Node
from vector2 import Vector2
class Graph(object):
    def __init__(self, dims):
        self.width = dims
        self.height = dims
        self.totalsize = self.width * self.height
        self.nodes = []
        id = 0
        for i in range(0, self.height):    
            for y in range(0, self.width):
                n = Node(id, Vector2(i,y))
                id = id + 1
                self.nodes.append(n)
class Node(object):
    def __init__(self, guid, pos):
        self.__guid = guid
        self.position = pos
    def find_neighbors(self,graph):
        valid_neighbors = []
        valid_neighbors.append(guid - self.dims)'''top_neighbor'''
        valid_neighbors.append(guid + self.dims)'''bot_neighbor'''
        valid_neighbors.append(guid - 1)'''left_neighbor'''
        valid_neighbors.append(guid + 1)'''right_neighbor'''
        valid_neighbors.append(guid - self.dims - 1)'''top_left'''
        valid_neighbors.append(guid - self.dims + 1)'''top_right'''
        valid_neighbors.append(guid + self.dims - 1)'''bot_left'''
        valid_neighbors.append(guid + self.dims + 1)'''bot_right'''
    def find_gscore(self,Node):
        if ((self.postion.xpos == Node.position.xpos and self.postion.ypos != Node.position.ypos) or
        (self.postion.xpos != Node.position.xpos and self.postion.ypos == Node.position.ypos)):
        self.g_score = Node.g_score + 10
        else:
         self.g_score = Node.g_score + 14
         return g_score
    def find_hscore(self,Node,other):
        h_score=((self.xpos - other.xpos and self.ypos - other.ypos * 10))
        return h_score 
    def find_fscore(self,Node,other):
        f_score = g_score + h_score
        return f_score
def main():
    g = Graph(10)
    a = Node(100)
    
        

main()