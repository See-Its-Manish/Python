# Function of Selection Sort
def Sort(l):
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if(l[i]>l[j]):
				l[i], l[j] = l[j], l[i]


def BS(l,n):
	lb = 0
	ub = len(l)-1
	while(lb<=ub):
		m = (lb+ub)//2
		if(l[m]==n):
			return m+1
		elif(l[m]>n):
			ub = m-1
		else:
			lb = m+1
	return -1


myList = [12,122,13,14,5,31,2,122,1]
Sort(myList)
print(myList)
print(BS(myList,-1))
