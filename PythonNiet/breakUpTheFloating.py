n= float(input("Enter a floating number: "))
# temp1=temp2=n
# intPart=int(temp1)
# floatPart=temp2-intPart
intPart = ceil(n)
n=n-intPart

print("Integer Part:",intPart,"Floating Part", floatPart)