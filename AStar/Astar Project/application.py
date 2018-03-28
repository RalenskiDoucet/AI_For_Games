import pygame
from shapesclass import Line
from shapesclass import Shape
from shapesclass import Rectangle
from vector2 import Vector2
from A_Star import Astar
from GraphAndNodeClass import Graph
from GraphAndNodeClass import Node1
class Application(object):
    def __init__(self, step_delay):
        pygame.init()
        self.step_delay = step_delay
        self.screen = pygame.display.set_mode((1080, 720))    
        self.running = True
        self.events = None

    def update(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            pygame.event.pump()
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:    
                    self.running = False
            self.draw()

    def draw(self):
        pygame.display.update()
        pygame.display.flip()  


def main():
    app = Application(0.1)
    app.update()
    r = Shape(100,10,50)
    s = Rectangle(Vector2(100, 100), (150, 100, 150), [50, 50],pygame , 0)
    s.draw()
    l = Line(Vector2(50,50),(75,75,75),[1,50] ,pygame)

main() 