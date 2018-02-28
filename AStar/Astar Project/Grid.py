'''A class that generates a graph and nodes in the graph.'''
class Node(object):
    def __init__(self,guid):
        self.guid=guid
class Graph(object):
    def __init__(self,dims):
        self.dims=dims
    def get_neighbors(self,Graph,dims):
        n = Node(5)
        g = Graph(4)
        top_neighbor = current.N- dims
        bottom_neighbor = current.Node + dims
        left_neighbor = current.Node - 1
        right_neighbor = current.Node + 1
        top_right_neighbor = top_neighbor + 1
        top_left_neighbor = top_neighbor - 1
        bottom_right_neighbor = bottom_neighbor + 1
        bottom_left_neighbor = bottom_neighbor-1
def _main_():
    n = Node(5)
    g = Graph(4)
_main_()
