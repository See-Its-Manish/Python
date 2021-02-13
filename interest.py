print("Enter Principal Amount, Time Period(in yrs) and rate(p.a.):")
p=float(input())
r=float(input())
t=float(input())

print("Compound Interest:",(p*((1+r)**t)-p))
