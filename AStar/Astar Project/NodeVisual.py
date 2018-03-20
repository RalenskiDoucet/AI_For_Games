import pygame
from shapesclass import Rectangle
from shapesclass import Line
from shapesclass import Text
from GraphAndNodeClass import Node
from GraphAndNodeClass import Graph
from vector2 import Vector2
from A_Star import Astar

class NodeVisual(object):
    def __init__(self, node, draw_pos, scale, draw_surface):
        self.node = node
        self.shape = Rectangle(draw_pos, (255, 255, 255), scale, draw_surface, 0)
        self.is_hoovered = False
        self.is_start = False
        self.is_goal = False
        self.is_path = False
        self.is_open = False
        self.is_closed = False
        self.show_scores = False
        self.border = Rectangle(draw_pos,(255, 255, 255), scale, draw_surface, 4)

    def update(self, events):
        self.node_clicked(events)                
        if not self.node.traversable:
            self.shape.change_color((0, 0, 0))
        elif self.is_closed and not self.is_start and not self.is_goal:
            self.shape.change_color((247, 143, 143))
        elif self.is_open and not self.is_start and not self.is_goal:
            self.shape.change_color((143, 183, 247))
        elif self.is_start:
            self.shape.change_color((0, 255, 0))
        elif self.is_goal:
            self.shape.change_color((255, 0, 0))
        else:
            self.shape.change_color((255, 255, 255))
        if self.is_hoovered:
            self.border.change_color((255, 0, 0))
        else:
            self.border.change_color((0, 0, 0))
            
    def reset_node(self):
        self.is_closed = False
        self.is_open = False
        self.is_path = False
        self.node.parent = None

    def draw(self, graph_visual):
        self.shape.draw()
        self.border.draw()        
        if self.node.parent is not None:
            par = graph_visual.get_visual(self.node.parent)
            line = pygame.draw.lines(self.shape.draw_surface, (0,255,0), True, 
            [[self.shape.position.x_pos + self.shape.scale[0] / 2, self.shape.position.y_pos + self.shape.scale[1] / 2],
            [par.shape.position.x_pos + par.shape.scale[0] / 2, par.shape.position.y_pos + par.shape.scale[1] / 2]], 1)
        if (self.is_open or self.is_closed or self.is_goal or self.is_start) and self.show_scores:
            text = Text(Vector2(5,5), (0,0,0), str(self.node.f_score), 12 , self.shape.draw_surface)
            text.draw_on_surface(self.shape.rect)
            text2 = Text(Vector2(25,20), (0,0,0), str(self.node.h_score), 12 , self.shape.draw_surface)
            text2.draw_on_surface(self.shape.rect)
            text3 = Text(Vector2(5,20), (0,0,0), str(self.node.g_score), 12 , self.shape.draw_surface)
            text3.draw_on_surface(self.shape.rect)

    def node_clicked(self, events):
        mouse_position = pygame.mouse.get_pos()
        if self.shape.rect.collidepoint(mouse_position):
            self.is_hoovered = True
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.node.traversable = not self.node.traversable            
        else:
            self.is_hoovered = False
  



                