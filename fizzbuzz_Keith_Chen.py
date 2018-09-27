n = 1
m = 101
for x in range (n, m):
	print (x)
	if ((x % 3) == 0) & ((x % 5) == 0):
		print ("FizzBuzz")
	elif (x % 3) == 0:
		print ("Fizz")
	elif (x % 5) == 0:
		print ("Buzz")