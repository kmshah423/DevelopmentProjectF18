def fizzbuzz(n=1, m=101):
    if (n >= m):
        return
    elif (n % 15 == 0):
        print("FizzBuzz")
    elif (n % 3 == 0):
        print("Fizz")
    elif (n % 5 == 0):
        print("Buzz")
    else:
        print(n)
    fizzbuzz(n + 1, m)


if __name__ == '__main__':
    fizzbuzz()
