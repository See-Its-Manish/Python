"""
***********How to iterate over list**************
"""
# List 
l=[1,2,3,4,5]

# Method 1
for i in l:
	print(i, end = " ")
print()		# For a new Line


# Method 2
length = len(l)
for i in range(0,length):
	print(l[i], end =  " ")
print()


# Method 3 (Similar to that of 2)
# We will use the above length variale
i=0
while( i < length):
	print(l[i], end = " ")
	i = i + 1	# This statement increases i by 1
print()


# Method 4
# Using List Comprehension
x = [print(i) for i in l]


# Method 5
for i, val in enumerate(l):
	print(i,"->",val)




# *************To find the mean of number in list******************

sumOfElements = 0

for i in l:
	sumOfElements+=i
print("Sum of Elements in List:",sumOfElements)
print("Average :",sumOfElements/len(l))



"""
*****************Tuple*******************
"""
#if a tuple has only one value then it must be defined as following
t = (1,)
# t=(1) is considered as a normal assignation of integer 1 to t
print(t)

tup = (1,2,3,4, "Last Element")

# Printing Methods
print(tup)
print(tup[0:3])

# Third(Jumps) in Slicing is called stride
print(tup[-1:-4:-1])


t1 = ("MY" , "NAME" , "IS", "MANISH")

# Checking if an element present in a tuple
if "MY" in t1:
	print("YES")
else:
	print("NO")


# If we try to concatinating two tuples than a new tuple is created
t2 = (1,2,3,4)
print(id(t1))	# Prints Memory Address
t1 = t1 + t2
print(id(t1))	# Now Memory Address is changed


# If a function returns multivariable then it is returned in the form of tuple
def getNum(*args):
	return (args)
w = getNum(1,2,3,4)
print(type(w))	# Tuple is retured


# Divmod returns in form of a tuple
r = divmod(10,5)
print(type(r))	# Prints class-> Tuple
a,b=divmod(10,5)
# Scattering of tuple
print(type(a),a)


# Zipping of tuple
tup1 = (1,2,3,4)
tup2 = ("First", "Second", "Third", "Four")
# Zip Zips elements in the form of tuple
# Zip returns a Zip Element which can be converted into iterables
tup3 = list(zip(tup1,tup2))
print(type(tup3) ,tup3)











