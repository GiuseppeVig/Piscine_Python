import sys

x = float(sys.argv[1])
i = len(sys.argv)
if (i != 4):
	print("Error! Usage: python3 ft_max.py <x> <y> <z>")
else:
	j = 2
	while (j < i):
		if (x < float(sys.argv[j])):
			x = float(sys.argv[j])
		j += 1
	print("the max is: " + str(x))
