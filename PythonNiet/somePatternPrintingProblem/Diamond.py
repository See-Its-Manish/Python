# Program to Print Diamond
n = int(input("Enter the length: "))

noOfSpaces = 2*n-3
noOfStars = 1

for i in range(0, n-1):
	for j in range(0, noOfSpaces):
		print(" ", end="")
	for k in range(0, noOfStars):
		print("* ", end="")
	print()
	noOfSpaces -= 2
	noOfStars += 2

for i in range(0, 2*n-1):
	print("* ", end="")
print()

noOfSpaces = 2
noOfStars = 2*n-3

for i in range(0, n-1):
	for j in range(0, noOfSpaces):
		print(" ", end="")
	for k in range(0, noOfStars):
		print("* ", end="")
	print()
	noOfSpaces += 2
	noOfStars -= 2




