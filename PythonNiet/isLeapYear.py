# Program to check whether the entered year is leap year or not
n1 = input("Enter the year: ")
n1 = int(n1)

isLeapYear = False
if n1 % 4 == 0 and n1 % 100 == 0 and n1 % 400 == 0:
    isLeapYear = True
 
if n1 % 4 == 0 and n1 % 100 != 0:
    isLeapYear = True


if isLeapYear:
    print("Leap Year")
else:
    print("Not Leap Year")