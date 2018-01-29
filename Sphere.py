import math

class Sphere(object):

	def __init__(self, radius = 1.0, x = 0.0, y = 0.0, z = 0.0):		
		self.radius = radius
		self.x = x
		self.y = y
		self.z = z

	def get_volume(self):
		return  4/3 * math.pi * (self.radius**3)

	def get_square(self):
		return 4 * math.pi * self.radius**2

	def get_radius(self):
		return self.radius

	def get_center(self):
		return (self.x, self.y, self.z)

	def set_radius(self, r):
		self.radius = r

	def set_center(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def is_point_inside(self, x, y, z):
		return (x - self.x)**2 + (y - self.y)**2 + (z - self.z)**2 <= self.radius**2