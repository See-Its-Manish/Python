def max(a,b):
	if(a>b): return a
	else: return b

print("Enter three numbers:")
n1=int(input())
n2=int(input())
n3=int(input())
print("Max of Three: ",max(n1,max(n2,n3)))