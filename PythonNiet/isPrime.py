import math

# INPUT
print("Enter a number: ", end="")
var = input()
var = int(var)

# PROCESS
isPrime = True
end = int(math.sqrt(var)) + 1
for i in range(2, end, 1):
    if(var % i) == 0:
        isPrime = False
        break

# OUTPUT
if isPrime:
    print("Prime")
else:
    print("Not Prime")
