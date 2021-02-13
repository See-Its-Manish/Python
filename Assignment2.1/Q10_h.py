n=int(input("Enter the Height: "))
print("*"*(2*n-1))

for i in range(n-1,1,-1):
	print(" "*(n-i), end="")
	print("*"," "*(2*i-3), "*", sep="")

print(" "*(n-1),"*", sep="")

