from vector2 import Vector2
class Graph(object):
   # '''A class that defines the properties of a graph.'''
    def __init__(self, dims):
        self.width = dims
        self.height = dims
        self.totalsize = self.width * self.height
        self.nodes = []
        id = 0
        for i in range(0, self.height):    
            for y in range(0, self.width):
                n = Node(Vector2(i,y))                
                self.nodes.append(n)    
        
class Node(object):
    #'''A class created to define the properties of a node.'''
    def __init__(self, pos):        
        self.position = pos
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.parent = None
        self.is_traversable = True
        self.neighbors = None
        self.is_goal = False
        self.is_start = False

    def find_neighbors(self,graph):
        # '''Gets the neighbors of the node. Used to generate the correct path for the user to test against'''
        valid_neighbors = []
        top = (self.position + Vector2(0, 1)) #Top_neighbor
        bottom = (self.position + Vector2(0, -1)) #Bottom_neighbor
        left = (self.position + Vector2(-1, 0)) #Left_neighbor
        right = (self.position + Vector2(1, 0)) #Right_neighbor
        top_right = (self.position + Vector2(1, 1)) #Top Right_neighbor
        top_left = (self.position + Vector2(-1, 1)) #Top Left_neighbor
        bottom_right = (self.position + Vector2(1, -1)) #Bottom Right_neighbor
        bottom_left = (self.position + Vector2(-1, -1)) #Bottom Left_neighbor
        valid_neighbors.append(top)
        valid_neighbors.append(left)
        valid_neighbors.append(right)
        valid_neighbors.append(bottom)
        valid_neighbors.append(top_left)
        valid_neighbors.append(top_right)
        valid_neighbors.append(bottom_left)
        valid_neighbors.append(bottom_right)   
        
        neighbors = []
        for n in graph.nodes:
            for pos in valid_neighbors:
                if n.position == pos:
                    neighbors.append(n)
        return neighbors

    def set_parent(self, other):
        #     '''Attempts to change the value of the parent variable. If the value is
        #None the parent is automaticly set to the value of node passed in. Otherwise
        #a new G score is calcualted and if it is cheaper than the current the parent
        #is changed to the node passed in and the G score is modified to reflect the
        #change in parents'''
        self.parent = other
        return self.parent
        
    def calculate_g_score(self, other):
        #  '''Calculates the movement cost to move from nodes parent to it self. If the
        #movement is horizontal or vertical the cost is parent's G score + 10. If the
        #movement is diagonal the cost is parent's G score + 14'''    
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
        # '''Calculates the estimated movement cost to move from this node to the goal.'''
        x_distance = abs(other.position.xpos - self.position.xpos)
        y_distance = abs(other.position.ypos - self.position.ypos)
        total = x_distance + y_distance
        self.h_score = total * 10
        return self.h_score

    def calculate_f_score(self):
        #  '''Calculates the fscore which is the sum of the H score and G score of the node'''
        self.f_score = self.g_score + self.h_score
        return self.f_score

    def set_not_traversable(self):
        #'''Makes a certain selected spot nontransversible.'''
        self.is_traversable = False

def main():
    g = Graph(10)    
    a = g.nodes[0].find_neighbors(g)
    a[0].calculate_g_score(g.nodes[0])
    a[1].calculate_g_score(g.nodes[0])
    a[2].calculate_g_score(g.nodes[0])
    b = 0;