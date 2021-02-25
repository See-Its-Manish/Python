"""
*****************MERGE SORT*******************
"""
# Function to merge Sorted Halves of given array
def mergeHalves(myList, leftStart, leftEnd, rightStart, rightEnd):
	left = leftStart
	right = rightStart
	index = 0
	toCopy =[0]*(rightEnd - leftStart+1)
	while(left <= leftEnd and right <= rightEnd):
		if(myList[left]<myList[right]):
			toCopy[index] = myList[left]
			left+=1
			index+=1
		else:
			toCopy[index] = myList[right]
			right+=1
			index+=1

	if (left > leftEnd):
		while(right <= rightEnd):
			toCopy[index]  = myList[right]
			index+=1
			right+=1
	

	if (right > rightEnd):
		while(left <= leftEnd):
			toCopy[index]  = myList[left]
			index+=1
			left+=1
	
	index=0
	while(index < len(toCopy)):
		myList[index+leftStart] = toCopy[index]
		index+=1


# Recursive Function of Merge Sort
def mergeSort(myList,start,end):

	if(start<end):
		mid = int((start + end)/2)
		mergeSort(myList,start,mid)
		mergeSort(myList,mid+1,end)
		mergeHalves(myList,start,mid,mid + 1, end)


# Declaration of list
myList = [12, 11, 13, 5, 6, 7, 12, 13, 11, 1]
mergeSort(myList,0,len(myList)-1)	# Function Call

# Printing of Sorted List
for i in myList:
	print(i, end=" ")