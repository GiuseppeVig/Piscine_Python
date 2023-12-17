class Point:
	def	__init__(self, x, y):
		self.x = x
		self.y = y

a, b = input("Insert the coordinates of the first point: ").split(",")
p1 = point(float(a), float(b))
c, d = input("Insert the coordinates of the second point:").split(",")
p2 = point(float(c), float(d))
function = ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**1/2
print(function)
