def max(a,b):
	if(a>b):
		return a
	else:
		return b

print("Enter three Numbers:")
a=int(input())
b=int(input())
c=int(input())
print(max(a,max(b,c)))
