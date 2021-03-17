def func(s):
	str = ""
	for i in range(len(s)):
		if(i%2==0):
			str +=s[i]
		else:
			str += chr(ord(s[i]) - 32)
	return str

print(func("strong"))