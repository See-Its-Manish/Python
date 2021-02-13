# To check if number is even or not.


n = input("Enter the number: ")
n = int(n)


if n == 1 or n == 0:
    print("Not Prime")
    exit(0)

isPrime = True
for i in range(2, n):
    if n % i == 0:
        isPrime = False
        break

if isPrime:
    print("Number is Prime")

else:
    print("Number is not Prime")
