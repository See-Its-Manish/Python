m1 = int(input("Enter Marks 1: "))
m2 = int(input("Enter Marks 2: "))
m3 = int(input("Enter Marks 3: "))

perc = ((m1+m2+m3)/300)*100
print("Percentage: ",perc,"%")

if(perc>=60):
	print("1st Division")
elif(perc < 60 and perc  >= 40):
	print("2nd Division")
elif(perc >= 10  and perc  < 40  ):
	print("3rd Division")
else:
	print("Fail")