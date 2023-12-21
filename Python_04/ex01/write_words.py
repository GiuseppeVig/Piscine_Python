def sort(array):
	for j in array:
		for i in [0, len(array) - 1]:
			if (i != len(array) - 1):
				if array[i]>array[i+1]:
					array[i], array[i+1] = array[i+1], array[i]

f = open("words.txt")
i = int(input("Insert an integer: "))
arr = []
for x in f:
	if (len(x) > i):
		arr.append(x)
sort(arr)
f2 = open("long_words.txt", "w")
for l in arr:
	f2.write(l)
print("The words longer than " + str(i) + " have been written on \"long_words.txt\"")
