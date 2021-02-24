def isPrime(n):
	if n==1 or n==0:
		return False
	for i in range(2,int((n)**0.5)+1):
		if n%i==0:
			return False
	return True


n = int(input("Enter a number: "))
if(isPrime(n)):
	print(f"{n} is Prime")
else:
	print(f"{n} is not Prime")