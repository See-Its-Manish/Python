l =[12,23,42]

print(len(l))
# for i in range(0,len(l)):
# 	print(l[i],end=" ")

"""
i----> 0
l[i]--->l[0=12


i--->1
l[i]-->l[1]=23




i---->2
l[i]--->l[2]=42



i---->3

i<len(l)---->3<3
false
"""
e = enumerate(l,start = 1)
print(e)