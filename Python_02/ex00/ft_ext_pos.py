import sys

if (len(sys.argv) == 1):
	print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
else:
	x = 1
	pos_min = 0
	pos_max = 0
	j = int(sys.argv[1])
	z = int(sys.argv[1])
	while (x < len(sys.argv)):
		if (j < int(sys.argv[x])):
			j = int(sys.argv[x])
			pos_max = x - 1
		if (z > int(sys.argv[x])):
			z = int(sys.argv[x])
			pos_min = x - 1
		x += 1
	print("The min is " + str(z) + " and its position is " + str(pos_min))
	print("The max is " + str(j) + " and its position is " + str(pos_max))


