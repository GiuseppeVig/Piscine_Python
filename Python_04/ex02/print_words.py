def sort(array):
	for j in array:
		for i in [0, len(array) - 1]:
			if (i != len(array) - 1):
				if array[i]>array[i+1]:
					array[i], array[i+1] = array[i+1], array[i]

try:
	f = open(input("Insert file name: "))
	i = int(input("Insert an integer: "))
	arr = []
	for x in f:
		if (len(x) > i):
			arr.append(x)
	sort(arr)
	print("The words longer than " + str(i) + " are the following:")
	for l in arr:
		print(l, end ="")
except:
	print("Error! The specified file does not exist!")
