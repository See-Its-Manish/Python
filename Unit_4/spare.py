# print("Enter your name:")
# name = input()
# print(name.center(10,"*"))
# name=name.capitalize()
# print(name)

# print("Enter your Message:")
# mess = input()

# n = mess.count("Manish",0 ,len(mess))

# print(n,type(n))


# end = mess.endswith("ish",0,len(mess))

# print(end,type(end))


# s = "Manish"
# print(id(s))

# s ="Sharma"
# print(id(s))

"""
%c ---> char
%d ---> Dec
%s ---> String
%f ---> float
"""
# print("enter your name")
# name =input()

# print("enter your age")
# age = int(input())

# str = "Your name is %s and Age is %d and float is %f"%(name,age,1.001)
# print(str)

# print(str.find("20"))


# str ="12345"

# print(str[-1:-6:-1])

# a = "A"
# while(a<=ord("Z")):
# 	print(ord(a), "-->", a)
# 	a=chr(ord(a)+1)



# A---Z ---> 65 -- 90

# a -- z ---> 97 -- 122

# 0---9 -----> 48  -- 57


s ="A"
for i in range(1,5):
	for j in range(i):
		print(s,end="")
		s = chr(ord(s)+1)
	s="A"
	print()

# List Comprehension
print([i**3 for i in range(11)])

l =[1,2,4]

cube = tuple(i*2 for i in l)
print(cube)

l.append(3)

l.insert(2,5)


l =[12,3,34,45,5,6,77,1]
max=-1
for i in range(len(l)//2,len(l)):
	if(l[i]>max):
		max =l[i]
print(max)

# int(len(l)/2) ----> len(l)//2
# 9/2=4.5

# int(len(l)/2) ------> len(l)
# 	4 ---------> 8
