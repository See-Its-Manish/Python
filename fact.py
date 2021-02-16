def fact(n):
	# Base Cases
	if n==1 or n==0:
		return 1
	# Self Work
	return n*fact(n-1)

# n=int(input("Enter a number: "))
# if(n<0):
# 	print("Negatives not allowed")
# 	exit()

# print(fact(n))	# prints n!



def fib(n):

	# Base Cases
	if( n==1 or n==0):
		return n

	# Self Work
	return fib(n-1) + fib(n-2)

print(fib(6))