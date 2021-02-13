n=int(input("Enter the year: "))
isLeapYear=False

if(n%4==0 and n%100==0 and n%400==0):
	isLeapYear=True

if(n%4==0 and n%100!=0):
	isLeapYear=True

if isLeapYear:
	print("Its a Leap year")
else: 
	print("Not a Leap year")