x = input("Insert a String: ")
y = int(input("Insert an integer: "))
if (y < len(x)):
	print(x[y] + " " + x[-y])
else:
	print("Index out of range")
