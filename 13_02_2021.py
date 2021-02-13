# Lambda Function for finding square
sq= lambda a:a**2
print(sq(4))	#Prints 16

# Lambda Function for Product of two number
product = lambda a,b:a*b
print(product(2,3))		# Prints 6

# Mapping with Lambda Function
number = [1, 3, 4, 6, 9]
myList1 = list(map(lambda x: x**2  , number))	# Maps Sqaure of each element of number in myList
print(myList1) # Prints [1, 9, 16, 36, 81]

# Filtering with Lambda Function
myList2 = list(filter(lambda x:x%2!=0,number)) # Filters Odd numbers in number
print(myList2)	# Prints [1, 3, 9]

