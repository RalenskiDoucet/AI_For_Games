class Shape(object):
#A class to make shapes
    def __init__(self, surface, color, pos):
        self.pos = pos
        self.color = color
        self.surface = surface

    def change_color(self, color):
        self.color = color

class Rectangle(Shape):
    def __init__(self, surface, color, pos, scale):
        Shape.__init__(self, surface, color, pos)
        self.scale = scale

    def draw_rect(self):
        pygame.draw.rect(self.surface, (self.color[0], self.color[1], self.color[2]),
        (self.pos.x_position, self.pos.y_position, self.scale[0], self.scale[1]))

class Line(Shape):
    
    def __init__(self, surface, color, start_pos, end_pos, width):
        Shape.__init__(self, surface, color, start_pos, end_pos, width)
        self.width = width

    def draw_line(self):
        pygame.draw.line(self.surface, (self.color[0], self.color[1], self.color[2]),
        (self.pos.x_position, self.pos.y_position), self.length)

class Circle(Shape):
    def __init__(self, surface, color, pos, radius):
        Shape.__init__(self, surface, color, pos)
        self.radius = radius

    def draw_circle(self):
        pygame.draw.circle(self.surface, (self.color[0], self.color[1], self.color[2]),
        (self.pos.x_position, self.pos.y_position), self.radius)