class Point:
	def	__init__(self, x, y):
		self.x = x
		self.y = y

class	Circle:
	def	__init__(self, x, y, r):
		self.center = Point(x, y)
		self.radius = r
	def	__str__(self):
		return ("Circle of center (" + str(self.center.x) + ", " + str(self.center.y) + ") and radius " + str(self.radius))

c = Circle(150, 100, 75)
print(c)

