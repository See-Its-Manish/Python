def Sort(l):
	for i in range(len(l)):

		for j in range(i+1,len(l)):

			if(l[i]>l[j]):
				temp = l[i]
				l[i] = l[j]
				l[j] = temp

	# return l


myList = [41,34, 45,43,2,1,1]

Sort(myList)

print(myList)

