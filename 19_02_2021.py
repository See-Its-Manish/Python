"""
********************* Tuples in Python *********************
"""
tup= (1,2,3,4)

print(tup)

"""
# Tuples are immutable
tup[0]  = 12 # It will give an error

"""
# Tuples are 0 based indexed

print(tup[0] , tup[1])





"""
********************* Lists in Python *************************
"""

# What is the Difference between tuple and list
"""
List are mutable that is we can add or update an element in List
"""
l=[1,2,3,4,5,6,7]

l.append(12)	# Appeding / Adding an elemet
l[0] = 11		# Updating in List

print(l)




"""
********* Slicing in List & Tuple ***********
"""

"""
Remember that while slicing we can only obtain values from the tuple 
But in list we can obtain as well as update the element in the list
"""
print(l[1:4])
print(tup[1:4])

l[1:3] = [100,200]	# Updating the list with slicing

# tup[1,2] = [10]	# This will give an error

print(l)	# l = [11,100,200,4,5,6,7]	# Updated index 1 with 100 and 2 with 200

"""
What is the use of tuple ???
Let's see
"""

def func():
	return 1,2,3,4,5

t=func()
print(type(t))	# type will be tuple
"""
There is general notion in programming that whenever a function is returning
something. We can't edit or change that value directly. You should make a custom copy of that
make changes to it. Tuples have significance when you need such data structure.
"""
toChange = list(func())	# This will new copy of tuple returned by the function
toChange[0] = 100
print(toChange)

"""
How to insert an element at specified position in a list
"""
# insert(postion, value) ----> syntax of insert()
l.insert(0 , "First")
l.insert(5, "Second")





"""
****************** Dictionary in Python (dict) **************************
"""
"""
Dictionary stores <key, value> pair in the form of list.
constraint: key is immutable but value can be anything.
Dictionary doesn't store values sequentially instead it stores in randomely
Dictionary stores value in the array of Linked List (Using Hashing)
Just like unordered map in C++ or HashMap in Java
If you don't know about hashing then just assume that dictionary stores element in random order 
"""

d={"Name":"Manish", "Age":18, "College":"NIET"}
print(d)
"""
print order may not be the same each time as that of storage time
"""
print(type(d))
"""
We can't make keys an mutable value
It will always take a immutable value
"""
# d1 = {[1,2,3]:"Value"} # This will give error <key,value> [1,2,3] -> list
# List is mutable and and key will always take immutable value and not mutable

d2 = {(1,2,3): "Value"}
#This Will work cause here key->(1,2,3) is a tuple(which is immutable)

"""
A dictioanry always have unique keys
A dictionary can't have two or more same key. Each key uniquely identifies its value
If you try to give same key more than once it will not add another <key, value> pair 
but update the value of existing key
Example:-
"""
d3= {"Name": "Manish" ,"Name": "Abhishek"}
print(d3)  # It will print "Name":"Abhishek" (Overriden the exitsing <"Name:Manish">)

"""
We can only Access Elements in dict using keys
"""
print(d["Name"], d["Age"]) # It will print Value at keys->(Name) & (Age) in d

# How to add <key,Value> pair in dict
d["State"] = "New Delhi" # Added <"State" : "New Delhi">
print(d)


"""
What if we try to access a value with a key which doesn't exist in our dict
"""
# print(d["Education"])	# Trying to search for key ->'Education' but will give error---> 'Key Error'

"""
If we use get() function to access values in dict
than it can handle above cases by giving None if a key doesn't 
exist in our dictionary
"""
print(d.get("Education")) # get returns None cause there is no such key 'Education' in our dict

'''
To delete a <key,value> pair
'''
del[d["State"]]	# Will delete <"State" : "New Delhi"> from our in dict
print(d) 

'''
How to empty our dict
'''
# d.clear()
# print(d)	# Prints empty list


'''
What if we want to print all keys in dict
'''

print(d.keys())	
print(type(d.keys()))	# This will show that type of d.keys() ----> dict_keys
'''
dict_keys is an iterable view of dictionary keys
You can iterate over dict_keys to get keys
'''
listOfKeys = []
for key in d.keys():	# key--->variable not a keyword
	listOfKeys.append(key)

# We have formed a list of keys in our dictinary
print(listOfKeys)


