c = str('A')
for i in range(1,7):
	for j in range(0,i):
		print(c,end= " ")
		c = chr(ord(c) + 1)
	print()