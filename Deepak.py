def func(l):
	pos6 = -1
	pos9 = -1
	for i in range(len(l)):
		if(l[i] == 6 and pos6 == -1):
			pos6 = i
		if(l[i] == 9 and pos9 == -1):
			pos9 = i
	
	sum = 0
	
	for i in range(len(l)):
		if(i>=pos6 and i<=pos9):
			continue
		sum += l[i]

	return sum

l1 = [1, 3, 5]
l2 = [4, 5, 6, 7, 8, 9]
l3 = [2, 1, 6, 9, 11]
l4 = [1,2,3,6,1,9,6,9]
print(func(l1), func(l2), func(l3), func(l4))