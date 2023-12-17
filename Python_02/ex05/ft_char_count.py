import sys

def sort(array):
	for j in range(0, len(array)-1):
		for i in range(0, len(array)-1):
			if array[i]>array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]

if (len(sys.argv) != 2):
	print("Error! No string given or too many arguments")
else:
	a = []
	for i in sys.argv[1]:
		if (i not in a):
			a.append(i)
	b = dict()
	sort(a)
	for j in a:
		temp = 0
		for i in sys.argv[1]:
			if (j == i):
				temp += 1
		b[j] = temp
	print("Char count:")
	for i in b:
		print(i, end=" = ")
		print(b[i])


