def isEqual(a,b):
	return (a==b)

print(isEqual(7,7))		# True
print(isEqual(2,7))		# False


def max(a,b):
	if(a>b):
		return a
	else:
		return b

print(max(2,max(3,4)))		# max(2,3,4) is 4

def permute(n,r):
	product=1
	for i in range(n,n-r,-1):
		product*=i
	return product

print(permute(6,2))		# 6n2=30


def gcd(a,b):
	for i in range(min(a,b),0,-1):
		if(a%i==0 and b%i==0):
			return(i)

print(gcd(20,28))		# Gcd of 20 and 28 is 4 

def lcm(a,b):
	for i in range(max(a,b), a*b+1):
		if(i%a==0 and i%b==0):
			return i

print(lcm(13,45))		#Lcm of 13 and 45 is 585


