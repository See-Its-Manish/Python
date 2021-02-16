# String Traversal
s  = "Welcome to Niet"
index=0
for i in s:
	print("s[%d] ="%(index),i)
	index+=1


# C style formatting in Python
print("Manish %s is %d years old"%("Sharma",18))
#%d-->Integer    %s----> String     %f--->float


# Mutability of strings in Python
a="Hello"
print(id(a))	# Printing Objects Unique(Memory Address of Object)
a+=" "			# Concatinating a space character
print(id(a))	# Memory Address is changed
a+="World"		# Concatinating "World" with string a
print(id(a))	# Memory Address have been changed


# 