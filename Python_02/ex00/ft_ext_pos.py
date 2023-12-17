import sys

if (len(sys.argv) == 1):
	print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
else:
	x = 1
	pos_min = 1
	pos_max = 1
	j = int(sys.argv[1], 10)
	z = int(sys.argv[1], 10)
	while (x < len(sys.argv)):
		if (j < int(sys.argv[x], 10)):
			j = int(sys.argv[x], 10)
			pos_max = x - 1
		if (z > int(sys.argv[x], 10)):
			z = int(sys.argv[x], 10)
			pos_min = x - 1
		x += 1
	print("The min is " + str(z) + " and its position is " + str(pos_min))
	print("The max is " + str(j) + " and its position is " + str(pos_max))


