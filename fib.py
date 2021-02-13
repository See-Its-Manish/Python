def fib(n):
	if(n==1 or n==0):
		return n
	return fib(n-1)+fib(n-2)


sumOfFibs=0
for i in range(1,6):
	sumOfFibs+=fib(i)

print("Sum of Fibanacci Number upto 6:",sumOfFibs)