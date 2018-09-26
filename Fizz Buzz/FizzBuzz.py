# Jose Garcia
# Group 6
# Assignment 1
# Write a program that prints numbers from 1 - 100,
# for multiples of 3 print "Fizz", for those of 5 print "Buzz",
# for those of 3 and 5 print "FizzBuzz"

def method(n):
    if n%3 == 0 and n%5 == 0:
        return 'FizzBuzz'
    elif n%5 == 0:
        return 'Buzz'
    elif n%3 == 0:
        return 'Fizz'
    else:
        return str(n)
    
def main():
    count = 0
    while count < 101:
        print(method(count))
        count = count + 1

main()
   
