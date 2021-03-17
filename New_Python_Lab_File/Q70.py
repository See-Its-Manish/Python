def merge(l,leftStart,rightEnd):
	leftEnd = (leftStart+rightEnd)//2
	rightStart = leftEnd+1
	left = leftStart
	right = rightStart
	temp = []
	while(left<=leftEnd and right<=rightEnd):
		if(l[left]<l[right]):
			temp.append(l[left])
			left +=1
		else:
			temp.append(l[right])
			right += 1

	if(left>leftEnd):
		while(right<=rightEnd):
			temp.append(l[right])
			right += 1
	if(right>rightEnd):
		while(left<=leftEnd):
			temp.append(l[left])
			left += 1

	l[leftStart : rightEnd+1] = temp[0 : len(temp)]  

def mergeSort(l,start,end):

	if(start>=end):
		return 
	mid = (start+end)//2
	mergeSort(l,start,mid)
	mergeSort(l,mid+1,end)
	merge(l,start,end)


l = [12,11,13,113,13,6,2927,272]  # [6,11,12,13,13,113,272,2927]
mergeSort(l,0,len(l)-1)
print(l)