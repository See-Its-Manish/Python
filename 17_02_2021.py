# Check if str in alpha numeric
s = "Abc123"
print(s.isalnum())
s1 = "Abc"
print(s1.isalnum())

# length of str
s2 = "Hello"
print(len(s2))	# Length = 5
# Multiline Strings
s3="""
Hello
World
"""
print(len(s3))	#Length = 13


# Slicing in Python

a="123456789"
print(a[:]) # Prints whole string
print(a[:6])# Prints till index 5 
print(a[2:6]) # prints from index 2 to 5
print(a[0:2]) # Prints from 0 to 1
print(a[1:20]) #Prints from 1 to 8 then truncates automatically
"""
Negative Slicing
 0  1  2  3  4  5  6  7  8 ---> Positve index
 1  2  3  4  5  6  7  8  9 ---> Value at that position
-9 -8 -7 -6 -5 -4 -3 -2 -1 ---> Negative Indexing
"""
print(a[-1:-10:-1]) # Prints from -1 to -10 with a -1 jump
print(a[2:-2:1]) # prints from 2 to -3 with +1 jump (Left to Right)

# Escape Sequence
"""
\' 		Single Quote 	
\\ 		Backslash 	
\n 		New Line 	
\r 		Carriage Return 	
\t 		Tab 	
\b 		Backspace 	
\f 		Form Feed 	
\\ooo 	Octal value 	(Ignore First backslash)
\\xhh 	Hex Value       (Igonre First backslash)
"""
print("manish\\MANISH")	# Printts manish\MANISH
print("MANISH\nSHARMA") # Prints MANISH (NEW LINE) SHARMA
print("MANISH\bSHARMA") # Prints MANISSHARMA
"""
Rest try at your own
"""