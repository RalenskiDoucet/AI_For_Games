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
   def create_grid(self):
        for m in range(0, self.width):
            for h in range(0, self.height):
                new_node = Node(Vector2(i, j))
                self.nodes.append(new_node)
class Node(object):
    def __init__(self, guid, pos):
        self.guid = guid
        self.position = pos
        self.g_score
        self.h_score
        self.f_score
    def find_neighbors(self,graph):
        valid_neighbors = [(node.position + Vector2(0, 1)), #Top
                          (node.position + Vector2(0, -1)), #Bottom
                          (node.position + Vector2(-1, 0)), #Left
                          (node.position + Vector2(1, 0)), #Right
                          (node.position + Vector2(1, 1)), #Top Right
                          (node.position + Vector2(-1, 1)), #Top Left
                          (node.position + Vector2(1, -1)), #Bot Right
                          (node.position + Vector2(-1, -1))] #Bot Left
        neighbors = []
        for n in self.nodes:
            for pos in valid_neighbors:
                if n.position == pos:
                    neighbors.append(n)
        return neighbors
    def set_parent(self, other):
        '''sets the parent of a node to another'''
        self.parent = other
        return self.parent
    def calculate_g_score(self, other):
        if self.parent is 0:
            if ((self.position.x_position is other.position.x_position and
                self.position.y_position is not other.position.y_position)
            or (self.position.x_position is not other.position.x_position and
                self.position.y_position is other.position.y_position)):
                self.g_score = other.g_score + 10
            else:
                self.g_score = other.g_score + 14
        elif self.parent is not None:
            tent_g = self.g_score
            if ((self.position.x_position is other.position.x_position and
                self.position.y_position is not other.position.y_position)
            or (self.position.x_position is not other.position.x_position and
                self.position.y_position is other.position.y_position)):
                tent_g = other.g_score + 10
            else:
                tent_g = other.g_score + 14
            if tent_g < self.g_score:
                self.g_score = tent_g
                self.set_parent(other)
    def calculate_h_score(self, other):
        x_distance = abs(other.position.x_position - self.position.x_position)
        y_distance = abs(other.position.y_position - self.position.y_position)
        total = x_distance + y_distance
        self.h_score = total * 10
        return self.h_score

    def calculate_f_score(self):
        self.f_score = self.g_score + self.h_score
        return self.f_score

    def set_not_traversable(self):
        self.is_traversable = False
def main():
    g = Graph(10)
    a = Node(100)
    n.find_neighbors(25)
    jk.calculate_g_score(25)
    jk.calculate_h_score
    jk.calculate_f_score(25)
    
        

main()