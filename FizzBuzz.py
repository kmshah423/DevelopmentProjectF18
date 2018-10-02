for x in range(101):
    if x == 0:
        continue
    if x % 3 != 0 and x % 5 != 0:
        print(x)
    if (x % 3) == 0 and (x % 5) == 0:
        print("FizzBuzz")
    else:
        if(x % 3) == 0:
            print("Fizz")
        else:
            if(x % 5) == 0:
                print("Buzz")
