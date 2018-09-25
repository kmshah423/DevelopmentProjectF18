print('What number would you like to start from?')
n = input();
print('What number would you like to go up to?')
m = input();

for i in range(n, m+1):
        if i%15 == 0:
            print 'FizzBuzz'
        elif i%5 == 0:
            print 'Buzz'
        elif i%3 == 0:
            print 'Fizz'
        else:
            print i
