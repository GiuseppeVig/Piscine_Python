x = int(input("Insert Hours: "))
x *= 3600
y = int(input("Insert Minutes: "))
y *= 60
z = int(input("Insert Second: "))
z += y + x
print("Total Seconds: " + str(z))
