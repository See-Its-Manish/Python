t = int(input())
while(t!=0):
	n = int(input())
	k = int(input())
	s = input()
    c=1
	for i in range(n-1):
		if s[i]==s[i+1] and s[i]=="*" and s[i+1]=="*":
			c+=1
		else:
			continue
	if c>=k:
		print("YES")
	else:
		print("NO")
