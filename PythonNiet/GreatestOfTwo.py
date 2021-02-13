# Program to find to find greatest of two number.

var1 = input("Enter first number: ")
var2 = input("Enter Second number: ")
var1 = int(var1)
var2 = int(var2)
if var1 > var2:
    print("Greatest of two numbers: ", var1)
elif var1 == var2:
    print("Both are same")
else:
    print("Greatest of two numbers: ", var2)