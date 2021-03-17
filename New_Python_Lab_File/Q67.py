def LS(myList,k):
	for i in range(len(myList)):
		if(myList[i] == k):
			return i+1
	return -1

l = [1,121,13,3,13,567,12,5]
print("Position of 3:",LS(l,3))
print("Position of 6:",LS(l,6))