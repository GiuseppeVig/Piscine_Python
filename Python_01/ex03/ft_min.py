import sys

def	my_min(elements = []):
	j = 0
	if (elements[1]):
		j = float(elements[1])
	i = len(elements) - 1
	while(i > 0):
		if (j > float(elements[i])):
			j = float(elements[i])
		i -= 1
	print("the min is: " + str(j))

i = len(sys.argv)
if (i != 4):
	print("Error! Usage: python3 ft_max.py <x> <y> <z>")
else:
	my_min(sys.argv)
