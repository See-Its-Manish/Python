num1 =int(input("Enter a number: "))
num2 =int(input("Enter a number: "))
num3 =int(input("Enter a number: "))

# Defining a function max to find max of two number

def max(a,b):
	if(a>=b):
		return a
	else:
		return b

greater = max(num1, max(num2, num3))	# First max(num2, num3) is computed, Lets say it is x
										# Then max(num1, x)

print(greater)