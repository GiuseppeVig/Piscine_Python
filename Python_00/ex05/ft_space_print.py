x = input("Insert a string: ")
y = len(x)
z = 0
if (y < 20):
	while (20 - z > y):
		print(" ", end = "")
		z += 1
	print(x)
else:
	m = x[y - 20:y:1]
	print(m)
