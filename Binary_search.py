def Binary_Search(a,k):
	l=0
	b=len(a)-1
	while(l<=b):
		m=int((l+b)/2)

		if(a[m]==k):
			return m+1
		elif(a[m]<k):
			l=m+1
		elif(a[m]>k):
			b=m-1

	return -1


a=[1,3,4,6,7,89]
print(Binary_Search(a,89))