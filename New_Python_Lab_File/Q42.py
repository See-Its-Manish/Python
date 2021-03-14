n = int(input("Enter the Height: "))
flag = 0 
for i in range(1,n+1):

	for j in range(2*i-1):
		if(flag==0):
			print("A",end="")
			flag=1
		else:
			print("B",end="")
			flag=0

	print()
