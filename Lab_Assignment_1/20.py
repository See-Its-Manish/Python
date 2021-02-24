n = int(input("Enter a Year: "))
isLeap=False
if(n%4==0 and n%100==0 and n%400==0):
	isLeap=True
if(n%4==0 and n%100!=0 ):
	isLeap=True

if(isLeap):
	print("Leap Year")
else:
	print("Not Leap Year")