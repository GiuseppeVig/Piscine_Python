x = input("Insert a String: ")
y = int(input("Insert an integer: "))
if (y < len(x)):
	z = x[y:(-y + 1):1]
	print(z)
else:
	print("Index out of range")
