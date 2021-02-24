print("Enter Principal Amount, Time Period(in yrs) and rate(p.a.):")
p=float(input())
r=float(input())
t=float(input())

print("Simple Interest:", (p*r*t)/100)
print("Compound Interest:",((p*((1+(r/100))**(t-1))))-p)
