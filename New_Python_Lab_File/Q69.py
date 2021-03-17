def sort(l):
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if(l[i]>l[j]):
				l[i],l[j] = l[j],l[i]

l = [12,12,23,44,1,2,3]
print("Original List,",l)
sort(l)
print("Sorted List: ",l)