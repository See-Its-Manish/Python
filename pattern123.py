# Integer


# chr ----> chr(integer) -----> character corresponding to that integer(ASCII)
A = 65
for i in range(1,6):
	for j in range(i):
		print(chr(A),end="")
		A+=1
	print()


