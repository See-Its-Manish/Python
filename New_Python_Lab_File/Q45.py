def combination(n,r):
	ans=1
	for i in range(n,n-r,-1):
		ans *=i
	
	for i in range(1,r+1):
		ans/=i

	return ans
	
print("Enter n and r (nCr): ")
n = int(input())
r = int(input())
print(combination(n,r))