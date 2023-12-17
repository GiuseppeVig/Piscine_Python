import sys

def ft_isspace(c, d):
	if (c == ' ' or d == ' '):
		return (True)
	return (False)

def palindrome():
	i = 0
	j = len(sys.argv[1]) - 1
	while (i != j and i != j - 1):
		if (ft_isspace(sys.argv[1][i], sys.argv[1][j]) != True and sys.argv[1][j] == sys.argv[1][i]):
			i += 1
			j -= 1
		elif (ft_isspace(sys.argv[1][i], sys.argv[1][j]) == True):
			if (sys.argv[1][i] == ' '):
				i += 1
			elif (sys.argv[1][j] == ' '):
				j -= 1
		else:
			break
	if (i != j and i != j - 1):
		return (False)
	else:
		return (True)

if (len(sys.argv) != 2):
	print("Error! Insert just 1 string!")
else:
	if (palindrome() == False):
		print("The string " + sys.argv[1] + " is not palindrome")
	else:
		print("The string " + sys.argv[1] +  " is palindrome")
