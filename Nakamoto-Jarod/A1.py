def FizzBuzz(N=0, M=100):
	for i in range(N,M):
		out = ""
		if i%3==0:
			out+="Fizz"
		if i%5==0:
			out+="Buzz"
		if out != "":
			print(out)
		else:
			print(i)
	
FizzBuzz()
FizzBuzz(10,15)