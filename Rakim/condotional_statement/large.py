def max(a,b):
	if(a>b):
		return a
	else:
		return b

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))
print("Max: ",max(max(a,b), max(d,c)))