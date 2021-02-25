n = int(input("Enter a number: "))

n1 = n
# Converting to Binary

b =[]
while(n1>0):
	 b.append(n1%2)
	 n1//=2

print(f"Binary of {n} is ",end = "")

for i in range(len(b)-1,-1,-1):
	print(b[i],sep="",end="")
print()