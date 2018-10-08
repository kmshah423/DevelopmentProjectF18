def fizz_buzz(n, m):
    for num in range(n, m + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")

        elif num % 3 == 0:
            print("Fizz")

        elif num % 5 == 0:
            print("Buzz")


fizz_buzz(1, 100)
