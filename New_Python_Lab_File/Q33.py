n = int(input("Enter number of terms: "))
s=0
e=1
print(0,1,end = " ")
for i in range(3,n+1):
	print(s+e,end=" ")
	s,e = e,s+e