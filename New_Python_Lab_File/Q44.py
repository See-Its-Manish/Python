def Compute(n):
	f=1
	s=0
	for i in range(1,n+1):
		f *= i
		s += i/f
	return s
n = int(input("Enter number of terms: "))
print("Sum of the series: ",Compute(n))