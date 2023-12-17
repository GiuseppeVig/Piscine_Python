class	Person:
	def	__init__(self, name, surname):
		self.name = name
		self.surname = surname

class	Student(Person):
	def	__init__(self, name, surname, yn=None, degree=None):
		self.name = name
		self.surname = surname
		self.yn = yn
		self.degree = degree
	def	__str__(self):
		if (self.yn == 'y'):
			return (self.name + " " + self.surname + " is registered to " + self.degree)
		else:
			return (self.name + " " + self.surname + " is not registered to any course")

n = input("Insert first name: ")
s = input("Insert last name: ")
y = input("Are you a student? (y/n)")
if (y != 'y' and y != 'n'):
	while (y != 'y' and y != 'n'):
		y = input("Please type \"y\" or \"n\": ")
if (y == 'y'):
	d = input("Please insert your degree course: ")
if (y == 'y'):
	aldo = Student(n, s, y, d)
else:
	aldo = Student(n, s)
print(aldo)
