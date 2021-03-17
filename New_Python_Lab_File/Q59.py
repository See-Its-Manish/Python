l = [112,111,21,112,23,42,354,566]
max = min = l[0]
avg = 0
for i in range(len(l)):
	if(max<l[i]):
		max = l[i]
	if(min>l[i]):
		min = l[i]
	avg += l[i]

avg = avg/len(l)

print("Maximum: ",max)
print("Minimum: ",min)
print("Averge: ", avg)