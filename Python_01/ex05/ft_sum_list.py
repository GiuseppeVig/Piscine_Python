def sum_list(elements = []):
	i = len(elements)
	j = 0
	while (i >= 0):
		j += int(elements[i - 1])
		i -= 1
	print("The sum is: " + str(j))

x = []
y = -1
z = 0
while (y != 0):
	y = int(input("insert integer: "))
	x.append(y)
	z += 1
sum_list(x)
