import sys

def trim(arr):
	arr[:] = arr[1:len(arr) - 1]

if (len(sys.argv) < 3):
	print("Error! You must insert at least 2 values")
else:
	a = sys.argv[1:len(sys.argv)]
	trim(a)
	print("The new list is: [", end = "")
	for i in a:
		print(i, end = "")
		if (i != a[len(a) - 1]):
			print(", " , end = "")
	print("]")

