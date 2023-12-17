import sys

if (len(sys.argv) <= 2):
	print("Error! You must insert at least 2 numbers")
else:
	sort = True
	i = len(sys.argv) - 1
	while (i > 1):
		if (int(sys.argv[i]) > int(sys.argv[i - 1])):
			print("The inserted sequence is not sorted!")
			sort = False
			break
		i -= 1
	if (sort == False):
		b = sys.argv[1:len(sys.argv)]
		a = sorted(b, reverse=True)
		print("The correct order is [", end = "")
		for i in a:
			print(i, end="")
			if (i != a[len(a) - 1]):
				print(", ", end="")
		print("]")
	else:
		print("The inserted sequence is sorted!")

