l = [112,111,21,112,23,42,354,566]
lb = 0
ub = len(l)-1


while(lb<ub):
	l[lb],l[ub] = l[ub],l[lb]
	lb+=1
	ub-=1

print(l)