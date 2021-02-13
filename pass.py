# n = int(input("Enter a number: "))
# # Checkinhg functionality with if statement
# if(n==1):
# 	print("in if")
# 	pass
# else:
# 	print("in else")
# 	print("Leaving else")

# Checking functionallity in loop and nested loop:

n1 = int(input("Enter a number: "))
for i in range(0,n1):
	print("in first loop for value of i:",i+1)
	for j in range(0,n1):
		if(j+1==2):
			pass
		else:
			print("in Else")
		print("in second loop for value of j:",j+1)
	print()
		
# Basically we can't left any if else block empty pass is used to 
# that area and do nothing
# Generally pass value is null

