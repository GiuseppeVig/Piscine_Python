import sys

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
	def	contains(self, x, y):
		if ((float(x) - self.center.x)**2 + (float(y) - self.center.y)**2 <= self.radius):
			print("The Point (" + str(x) + ", " + str(y) + ") lies in the Circle of center (" + str(self.center.x) + ", " + str(self.center.y) + ") and radius" + str(self.radius))
		else:
			print("The Point (" + str(x) + ", " + str(y) + ") lies out of the Circle of center (" + str(self.center.x) + ", " + str(self.center.y) + ") and radius" + str(self.radius))

x = sys.argv[1]
y = sys.argv[2]
c = Circle(0, 0, 1)
c.contains(x, y)
