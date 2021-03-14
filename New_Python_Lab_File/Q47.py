def fact(n):
	p =1 
	for i in range(2,n+1):
		p  *= i
	return p


n = int(input("Enter a number: "))
print(f"Factorial of {n} : {fact(n)}")
