"""
A
BA
BAB
ABAB
"""
flag=0
for i in range(1,6):	 # Line Change
	for j in range(i):	 # For pattern
		if(flag==0):
			print("A",end="")
			flag = 1
		else:
			print("B",end="")
			flag = 0
	print()