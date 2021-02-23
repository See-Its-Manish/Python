"""
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""
"""
rowCi+1 = ((row - i)/(i+1))*rowCi
"""
import math as m
n = int(input("Enter the Height:"))
print(1)
for row in range(1,n):
	print(1,end = " ")
	pe=1
	for i in range(0, row-1):
		pe = m.ceil(pe * ((row - i)/(i+1)))
		print(pe,end = " ")
	print(1)