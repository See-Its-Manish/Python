# Recursive function to get nth Fibonacci
def fib(n):
	if(n==1 or n==0):
		return n
	return fib(n-1)+fib(n-2)

# Input
n=int(input("Enter a number: "))
sumOfSeries=0
# Calculating the sum of series
for i in range(1,n):
	sumOfSeries+=fib(i)

print("Sum upto %d terms:"%(n), sumOfSeries)
