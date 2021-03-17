def BS(myList,k):
	lb = 0 
	ub =len(myList)
	while(lb<=ub):
		m = (lb+ub)//2
		if(myList[m]==k):
			return m+1
		elif(myList[m]>k):
			ub = m-1
		else:
			lb = m+1
	return -1

l = [12,23,44,54,65,87,100]
print("Position of 65:",BS(l,65))
print("Position of 11:",BS(l,11))