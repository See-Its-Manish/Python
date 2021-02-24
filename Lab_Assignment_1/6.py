print("Enter Sides of Triangle :")
a = int(input())
b = int(input())
c = int(input())

s = (a+b+c)/2

area = (s*(s-a) + s*(s-b) + s*(s-c))**0.5

print("Area:", area)