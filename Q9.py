import math as m

def isPrime(n):
	'''
	This function will check whether a number is prime or not
	'''
	if n==1 or n==0:
		return False
	for i in range(2,int(m.sqrt(n)+1)):
		if(n%i==0):
			return False
	return True


#Range input-->[s,e]
s=int(input("Enter the starting of range: "))
if(s<2):
	s=2
e=int(input("Enter the ending of range: "))

'''
We will check for for all integers in [s,e]
Sum of n terms in AP: n/2[2a + (n – 1)d]
We will take d=1, a=s, n=e-s+1
'''


#Calculating the sum of Primes
sumOfPrimes=0
for i in range(s,e+1):
	if(isPrime(i)==True):		# Checking if number is Prime or not
		sumOfPrimes+=i



'''
Now we have computed the sum of primes in [s,e]
Therefore sum of composites= (total sum in [s,e]) - sum of primes
Computing the required values
'''

n=e-s+1		# Number of terms in our Range/AP
totalSum = (n/2)*(2*s + (n-1))		# As d=1
sumOfComposites=totalSum-sumOfPrimes


#Printing the output
print("Sum of primes:",sumOfPrimes)
print("Sum of Composites:", sumOfComposites)

