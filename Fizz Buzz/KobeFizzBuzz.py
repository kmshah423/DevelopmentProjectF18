def method(n, m):
    for i in range(n, m+1):
        if i%3 == 15:
            print 'FizzBuzz'
        elif i%5 == 0:
            print 'Buzz'
        elif i%3 == 0:
            print 'Fizz'
        else:
            print i


def main():
    print('What number would you like to start from?')
    x = input()
    print('What number would you like to go up to?')
    y = input()
    method(x, y)


main()