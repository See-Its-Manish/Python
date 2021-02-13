def printMenu():
	print("Choose from the Menu:-")
	print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
	print("Enter Your Choice:", end=" ")

while(True):
	# Printing Of Menu
	printMenu()
	n=int(input())

	#Checking Condition For Wrong Input
	if n not in [1,2,3,4,5]:
		print("Wrong Input\n\n")
		continue

	# For Exit From the Calculator
	if(n==5): 
		exit(0)

	#Input
	n1=int(input("Enter first number: "))
	n2=int(input("Enter Second number: "))
	
	#Printing of Output
	if(n==1): print("Answer:",n1+n2) 
	elif(n==2): print("Answer:",n1-n2) 
	elif(n==3): print("Answer:",n1*n2) 
	elif(n==4): print("Answer:",n1/n2) 
		
	print()	