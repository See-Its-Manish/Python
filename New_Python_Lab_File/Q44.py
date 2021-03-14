n = int(input("Enter number of terms: "))
f=1
s=0
for i in range(1,n+1):
	f *= i
	s += i/f

print("Sum of the series: ",s)