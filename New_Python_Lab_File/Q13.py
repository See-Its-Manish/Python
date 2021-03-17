n = int(input("Enter Seconds: "))
hr = n//3600
n -= hr*3600
day = hr//24
hr -= day*24
mi = n//60
n -= mi*60
sec = n
print(f"{day}days {hr}hr {mi}min {sec}s")
