import sys

def sum_rows(list):
	print("The sum over rows is:")
	print("[ ", end = "")
	for row in range(int(sys.argv[1])):
		i = 0.0
		for column in range(int(sys.argv[2])):
			i += float(list[row][column])
		print(float(i), end = "")
		if (row + 1 != int(sys.argv[1], 10)):
			print(", ", end="")
	print("]")

def sum_columns(list):
	print("The sum over columns is:")
	print("[ ", end = "")
	for column in range(int(sys.argv[2])):
		i = 0.0
		for row in range(int(sys.argv[1])):
			i += float(list[row][column])
		print(float(i), end = "")
		if (column + 1 != int(sys.argv[2], 10)):
			print(", ", end="")
	print("]")

if (len(sys.argv) != 3):
	print("Error! Usage: python3 ft_matrix.py <n> <m>")
else:
	matrix = []
	for row in range(int(sys.argv[1])):
		a = []
		for column in range(int(sys.argv[2])):
			a.append(int(input("Insert the element in position (" + str(row) + "," + str(column) + "):")))
		matrix.append(a)
	print("The inserted matrix is:")
	for row in range(int(sys.argv[1])):
		print("[ ", end = "")
		for column in range(int(sys.argv[2])):
			print(float(matrix[row][column]), end="")
			if (column + 1 != int(sys.argv[2], 10)):
				print(", ", end="")
		print("]")
	sum_rows(matrix)
	sum_columns(matrix)



