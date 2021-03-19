def sort(l):
	for i in range(len(l)):
		small = l[i]
		index = i
		for j in range(i+1,len(l)):
			if(small>l[j]):
				small = l[j]
				index = j
		l[i], l[index] = l[index], l[i]

l = [12,112,4,2,2,4421,12]
sort(l)
print(l)