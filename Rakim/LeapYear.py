year = int(input("Enter year: "))

# Ladder if (Sirri)
if(year%4==0 and year%100==0 and year%400==0):
	print("Leap Year")
elif(year%4==0 and year%100!=0):
	print("Leap Year")
else:
	print("Not LY")


# Nested if (Chiriya ka ghosla)
if(year%4==0):
	if(year%100==0):
		if(year%400==0):
			print("LY")
		else:
			print("NLY")
	else:
		print("LY")
else:
	print("NLY")