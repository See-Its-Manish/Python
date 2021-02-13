# Program to check given number is Palindrome or not.

n = input("Enter a number: ")
n = int(n)
toComp = int(n)

rev = 0
while n > 0:
    rev = (rev * 10) + int(n % 10)
    n = n // 10

if toComp == rev:
    print("Given Number is Palindrome ")
else:
    print("Given Number is not Palindrome")

