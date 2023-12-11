x = int(input("Insert Hours: "), 10)
x *= 3600
y = int(input("Insert Minutes: "), 10)
y *= 60
z = int(input("Insert Second: "), 10)
z += y + x
print("Total Seconds: " + str(z))
