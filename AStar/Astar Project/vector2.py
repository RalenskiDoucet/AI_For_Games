"""A class to a Vector2"""
class Vector2(object):
	def __init__(self, xpos, ypos):
    		'''The inital decleration of the global class variables.'''
		self.xpos = xpos
		self.ypos = ypos
	def __add__(self, other):
			'''A function to add two Vect2s.'''
			new_vector = Vector2(self.xpos + other.xpos,self.ypos + other.ypos)
			return new_vector
	def __sub__(self, other):
			'''A Function to subtract two vect2s.'''
			new_vector = Vector2(self.xpos - other.xpos, self.ypos - other.ypos)
			return new_vector
	def multiplybyscalar(self, other):
			'''A Function to multiply a vect2 by the scalar.'''
			new_vector =Vector2(self.xpos * other,self.ypos * other)
			return new_vector
	def dot(self, other):
			'''A function that returns the dot product of two vectors.'''
			new_vector = Vector2(self.xpos * other.xpos,self.ypos * other.ypos)
			return new_vector
	def magnitude(self):
			'''A function that returns the magnitude of two vectors.'''
			new_vector = Vector2(self.xpos * self.xpos, + self.ypos *self.ypos)
			return new_vector
	def __normalize__(self):
			'''A function that normalizes a vector.'''
			new_vector = Vector2(self.xpos / self.magnitude(), self.ypos / self.magnitude())
			return new_vector
	#implent override for comaprison
	def __eq__(self, other):
		'''A function that overloads the compairson operator.'''
		return self.xpos == other.xpos and self.ypos == other.ypos
		