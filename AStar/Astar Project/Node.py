from vector2 import Vector2
from GraphAndNodeClass import Graph
class Node(object):
    def __init__(self, pos):        
        self.position = pos
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.parent = None
        self.is_traversable = True

    def find_neighbors(self,graph):
        valid_neighbors = [(self.position + Vector2(0, 1)), #Top_neighbor
                          (self.position + Vector2(0, -1)), #Bottom_neighbor
                          (self.position + Vector2(-1, 0)), #Left_neighbor
                          (self.position + Vector2(1, 0)), #Right_neighbor
                          (self.position + Vector2(1, 1)), #Top Right_neighbor
                          (self.position + Vector2(-1, 1)), #Top Left_neighbor
                          (self.position + Vector2(1, -1)), #Bottom Right_neighbor
                          (self.position + Vector2(-1, -1))] #Bottom Left_neighbor
        neighbors = []
        for n in graph.nodes:
            for pos in valid_neighbors:
                if n.position == pos:
                    neighbors.append(n)
        return neighbors

    def set_parent(self, other):
        self.parent = other
        return self.parent
        
    def calculate_g_score(self, other):
        if self.parent is None:
            if ((self.position.xpos is other.position.xpos and self.position.ypos is not other.position.ypos)
            or (self.position.xpos is not other.position.xpos and self.position.ypos is other.position.ypos)):
                self.g_score = other.g_score + 10
            else:
                self.g_score = other.g_score + 14
                self.set_parent(other)
        elif self.parent is not None:
            tentative_g = self.g_score
            if ((self.position.xpos is other.position.xpos and self.position.ypos is not other.position.ypos)
            or (self.position.xpos is not other.position.xpos and self.position.ypos is other.position.ypos)):
                tentative_g = other.g_score + 10
            else:
                tentative_g = other.g_score + 14
            if tentative_g < self.g_score:
                self.g_score = tentative_g
                self.set_parent(other)

    def calculate_h_score(self, other):
        x_distance = abs(other.position.xpos - self.position.xpos)
        y_distance = abs(other.position.ypos - self.position.ypos)
        total = x_distance + y_distance
        self.h_score = total * 10
        return self.h_score


    def calculate_f_score(self):
        self.f_score = self.g_score + self.h_score
        return self.f_score

    def set_not_traversable(self):
        self.is_traversable = False
