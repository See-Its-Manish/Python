def isPrime(n):
	if n==1 or n==0:
		return False
	for i in range(2,int((n)**0.5)+1):
		if n%i==0:
			return False
	return True

print("Enter the Starting and Ending of Interval[s,e] : ")
s = int(input())
e = int(input())
sumOfPrimes = 0
for i in range(s,e+1):
	if(isPrime(i)):
		sumOfPrimes +=i

print(f"Sum of Primes in range [{s},{e}] is {sumOfPrimes}")