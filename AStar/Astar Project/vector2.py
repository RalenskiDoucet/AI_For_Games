"""A class to a Vector2"""
class Vector2(object):
	def __init__(self, xpos, ypos):
    		'''The inital decleration of the global class variables.'''
		self.x_pos = xpos
		self.y_pos = ypos
	def __add__(self, other):
			'''A function to add two Vect2s.'''
			new_vector = Vector2(self.x_pos + other.x_pos,self.y_pos + other.y_pos)
			return new_vector
	def __sub__(self, other):
			'''A Function to subtract two vect2s.'''
			new_vector = Vector2(self.x_pos - other.x_pos, self.y_pos - other.y_pos)
			return new_vector
	def multiplybyscalar(self, other):
			'''A Function to multiply a vect2 by the scalar.'''
			new_vector =Vector2(self.x_pos * other,self.y_pos * other)
			return new_vector
	def dot(self, other):
			'''A function that returns the dot product of two vectors.'''
			new_vector = Vector2(self.x_pos * other.x_pos,self.y_pos * other.y_pos)
			return new_vector
	def magnitude(self):
			'''A function that returns the magnitude of two vectors.'''
			new_vector = Vector2(self.x_pos * self.x_pos, + self.y_pos *self.y_pos)
			return new_vector
	def __normalize__(self):
			'''A function that normalizes a vector.'''
			new_vector = Vector2(self.x_pos / self.magnitude(), self.y_pos / self.magnitude())
			return new_vector
	def __eq__(self, other):
		'''A function that overloads the compairson operator.'''
		return self.x_pos == other.x_pos and self.y_pos == other.y_pos
		