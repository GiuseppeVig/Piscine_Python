x = input("Insert an expression: ")
y = eval(x)
if (y < 0):
	y *= -1
print("The result is: " + str(y))
