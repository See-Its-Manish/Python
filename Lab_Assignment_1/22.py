def min(a,b):
	if(a>b): return b
	else: return a
print("Enter three numbers: ")
a = int(input())
b = int(input())
c = int(input())

print("Minimum of Three: ",min(a,min(b,c)))