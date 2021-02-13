# Program to check if given number is Armstrong.
import math
n = input("Enter a number: ")
n = int(n)

toComp = int(n)
numOfDigit = int(math.log10(n))+1  # This function will find number of digits in given number
isOver = 0
isOver = int(isOver)
sumOfNum = 0
sumOfNum = int(sumOfNum)
while isOver != numOfDigit:
    r = n % 10
    sumOfNum += r**numOfDigit
    n //= 10
    isOver += 1


if toComp == sumOfNum:
    print("Armstrong number")
else:
    print("Not Armstrong")
