import sys

if (len(sys.argv) != 2):
	print("Error! Usage: python3 ft_summorial.py <n>")
elif (int(sys.argv[1]) < 0):
	print("Error! n must be >=0")
else:
	x = int(sys.argv[1])
	j = 0
	while (x > 0):
		j += x
		x-= 1
	print("The sum is : " + str(j))
