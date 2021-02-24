"""
**************Linear Search****************
In Linear Search we iterate over every element(let's say i) and compare every ith element 
in the our list with the given number.
If the number if found, we return the position else we return -1
"""
print("**********FOR LINEAR SEARCH********")
l = [1,3,435, 66,7,8,8,9]
n = int(input("Enter the number to Search: "))
pos=-1
for i in range(0,len(l)):
	if(l[i] ==n):
		pos = i+1
print(f"{n} is found on index: {pos}")




"""
*********************Binary Search******************
for Binary Search 
Necessary Conditions:
1) List Should be Sorted
"""
print("**********FOR BINARY SEARCH********")
SL = [1,2,4,6,9,10]	# Sorted list
n = int(input("Enter the number to Search: "))
lb = 0	# Lower Bound
ub = len(SL)-1	# Upper Bound
pos = -1
while(lb<=ub):
	m = (lb+ub)//2
	if(SL[m] == n):
		pos = m+1
		break
	elif(SL[m]>n):
		ub = m-1
	elif(SL[m]<n):
		lb = m+1
print(f"Element {n} found at Position: {pos}")


"""
Why we do Binary Search if there is Linear Search?

Worst Time Complexity of Linear Search:
O(n)
Worst Time Complexity of Binary Search:
O(log(n))

n >>> log(n)

Hence Binary Search is very efficient than linear search
Only Drawback of Binary Search is it demands the list to sorted
"""


