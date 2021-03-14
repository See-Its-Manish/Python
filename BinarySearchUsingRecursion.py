def BS(myList,n,l,b):
	if(l>b):
		return -1

	m = (l+b)//2

	if(myList[m] == n):
		return m+1
	elif(myList[m]>n):
		return	BS(myList,n,l,m-1)
	else:
		return	BS(myList,n,m+1,b)



l = [1,2,3,4,5,6]

print(BS(l,17,0,len(l)-1))