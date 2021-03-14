print("Enter the coefficient of x^2 , x and constant: ")
a = int(input())
b = int(input())
c = int(input())

d = (b**2) - 4 * a * c

x1 = (-b + (d**0.5))/(2*a)
x2 = (-b - (d**0.5))/(2*a)

print(f"Roots are {x1} and {x2}")