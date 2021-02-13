def sum(n):
	if n==1 or n==0:	# Base Cases
		return n
	return n+sum(n-1)	# Self Work

n=int(input("Enter a number: "))
if(n<0):	# Checking for a negative number
	print("Negatives not allowed")
	exit()
print(sum(n))	

# for i in range(1,n+1):
# 	print("Sum:",sum(i))