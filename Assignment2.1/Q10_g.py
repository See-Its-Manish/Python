n=int(input("Enter the Height: "))
print("*"*n)
for i in range(2,n):
	print("*"," "*(n-2),"*",sep="")
print("*"*n)