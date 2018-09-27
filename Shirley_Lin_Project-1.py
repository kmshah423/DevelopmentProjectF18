def Fizzbuzz(n,m):
    if (n<=m):
        if (i%3==0):
            print('Fizz')
        elif (i%5==0):
            print('Buzz')            
        elif (i%3==0 and i%5==0):
            print('FizzBuzz')
        else:
            print(n)
            return Fizzbuzz(n+1,b)
    else:
             return 0

Fizzbuzz(1,100)
