def sort(array):
	for j in range(0, len(array)-1):
		for i in range(0, len(array)-1):
			if array[i]>array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]

f = open("words.txt")
i = int(input("Insert an integer: "))
arr = []
for x in f:
	if (len(x) > i):
		arr.append(x)
sort(arr)
print("The words longer than " + str(i) + " are the following:")
for l in arr:
	print(l, end ="")
