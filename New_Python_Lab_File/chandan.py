import math as m
n = int(input("Enter n: "))
r = int(input("Enter r: "))
ans = m.factorial(n) / (m.factorial(r) * m.factorial(n-r))
print(ans)