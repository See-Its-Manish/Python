def min(a,b):
	if(a>b):
		return b
	else:
		return a
print("Enter Three Numbers: ")
a = int(input())
b = int(input())
c = int(input())
print("Smallest: ",min(a,min(b,c)))