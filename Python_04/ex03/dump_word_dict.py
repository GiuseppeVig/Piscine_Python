import pickle

def sort(array):
	for j in range(0, len(array)-1):
		for i in range(0, len(array)-1):
			if array[i]>array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]

f = open("words.txt")
arr = []
lines = []
for x in f:
	if (len(x.strip()) not in arr):
		arr.append(len(x.strip()))
	lines.append(x)
sort(arr)
b = {}
for i in arr:
	b[i] = int(0)
for l in lines:
	b[len(l.strip())] += 1
with open("word_count.pickle", "w") as data:
	data.write(str(b))
