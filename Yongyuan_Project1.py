#Using loop
for i in range (1,101):
    if i%3 == 0:
        if i%5 ==0:
            print ('FizzBuzz')
        else:
            print ('Fizz')
    elif i%5 ==0:
        print ('Buzz')
    else:
        print (i)

#Funciton
def Fizzbuzz(n,m):
	for i in range (n,m):
		if i%3 == 0:
			if i%5 ==0:
				print ('FizzBuzz')
			else:
				print ('Fizz')
		elif i%5 ==0:
			print ('Buzz')
		else:
			print (i)

#Test function
Fizzbuzz(1,200)

#Using recursion instead of loop
def FB(a,b):
	if a<=b:
		if a%3 == 0:
			if a%5 ==0:
				print ('FizzBuzz')
			else:
				print ('Fizz')
		elif a%5 ==0:
			print ('Buzz')
		else:
			print (a)
		return FB(a+1,b)
	else:
		return 0

#Test funciton
FB(1,100)
