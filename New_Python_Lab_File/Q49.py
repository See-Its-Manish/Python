def fact(n):
	# Base Cases
	if(n==1 or n==0):
		return 1
	return n * fact(n-1)


n = int(input("Enter a number: "))
print(f"Factorial of {n} is {fact(n)}")