"""A class to a Vector2"""
class Vector2(object):
	def __init__(self, xpos,ypos):
		self.xpos=xpos
		self.ypos=ypos

	def __add__(self,other):
		'''A function to add two Vect2s'''
		new_vector = Vector2 (self, xpos + other.xpos and self, ypos + other.ypos)
		return new_vector

	def __sub__(self,other):
		'''A Function to subtract two vect2s'''
		new_vector = Vector2 (self, xpos-other.xpos and self, ypos-other.ypos)
		return new_vector
	
	def multiplybyscalar(self,other):
		'''A Function to multiply a vect2 by the scalor'''
		new_vector = Vector2 (self, xpos^2 and self, ypos^2)
		return new_vector
	