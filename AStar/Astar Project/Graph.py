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
        self.guid = guid
        self.position = pos
        self.g_score
        self.h_score
        self.f_score
    def find_neighbors(self,graph):
        top_neighbor=self.position-self.dims
        bot_neighbor=self.position+self.dims
        left_neighbor=self.position-1
        right_neighbor=self.position+1
        top_left_neighbor=top_neighbor-1
        top_right_neighbor=top_neighbor+1
        bot_left_neighbor=bot_neighbor-1
        bot_right_neighbor=bot_neighbor+1
        valid_neighbors=[]
        valid_neighbors.append(top_neighbor)
        valid_neighbors.append(top_left_neighbor)
        valid_neighbors.append(top_right_neighbor)
        valid_neighbors.append(bot_neighbor)
        valid_neighbors.append(bot_left_neighbor)
        valid_neighbors.append(bot_right_neighbor)
        valid_neighbors.append(left_neighbor)
        valid_neighbors.append(right_neighbor)
    def find_gscore(self,Node,g_score):
        if ((self.postion.xpos == Node.position.xpos and self.postion.ypos != Node.position.ypos) or
        (self.postion.xpos != Node.position.xpos and self.postion.ypos == Node.position.ypos)):
            self.g_score = Node.g_score + 10
        else:
         self.g_score = Node.g_score + 14
         return g_score
    def find_hscore(self,Node,h_score):
        h_score=((self.xpos - other.xpos and self.ypos - other.ypos * 10))
        return h_score 
    def find_fscore(self,Node,f_score):
        self.f_score = g_score + h_score
        return f_score
def main():
    g = Graph(10)
    a = Node(100)
    n.find_neighbors(25)
    jk.find_gscore(25)
    jk.find_hscore(25)
    jk.find_fscore(25)
    
        

main()