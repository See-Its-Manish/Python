def isPrime(n):
	if(n==0 or n==1):
		return False
	for i in range(2,int(n**0.5)+1):
		if(n%i==0):
			return False
	return True


print("Enter the range[s,e]: ",end="")
s=int(input())
e=int(input())

for i in range(s,e+1):
	if(isPrime(i)):
		print(i,end=" ")

