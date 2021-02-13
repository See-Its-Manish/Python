# Program to find sum of all digits in a number.
n1 = input("Enter a number: ")
n1 = int(n1)


sumOfDigits = 0
while n1 > 0:
    sumOfDigits += n1 % 10
    n1 = n1 // 10


print("Sum of Digits: ", sumOfDigits)
