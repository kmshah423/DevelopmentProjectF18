'''
An example project for dev project 1 (Fall 2018).
Project 1:

Write a program that prints the numbers from 1 to 100.
However, for multiples of 3 print to console "Fizz" and for multiples of 5 print to console "Buzz".
Also for numbers that are both multiples of 3 and 5 print to console "Fizz Buzz".

Optional/Bonus:
1) Write an additional function that prints the numbers n to m following above.
2) See if you can do FizzBuzz with out using a loop.

Used With California Polytechnic University California, as an example for Development Project Fall 2018
Author: Christopher Leal
Project Manager: Christopher Leal
Writing Date: 19 Sept, 2018
Finished: ~9/19/2018

'''

#___Imports___
from colorsys import *

#___Constants/Globals___



#___Functions___

def menu():
    '''
    a display menu that will show the results for all three parts to project 1
    '''
    while 1:
        print('\x1b[1;0;0m'
            "_______________________________\n" +
            "| 1) Normal Fizz Buzz          |\n" +
            "| 2) Function accepting n to m |\n"+
            "| 3) No loop Fizz Buzz         |\n" +
            "| 4) Exit                      |\n"
            "________________________________" +
            '\x1b[0m')

        choice = int(input("Your choice: "))

        if(choice == 1):
            __normal_fizz_buzz()
        elif(choice == 2):
            __nm_fizz_buzz()
        elif(choice == 3):
            print("Fizz Buzz without loop__________")
            __r_fizz_buzz(1,101)
            print("End Fizz Buzz without loop__________")
        elif(choice == 4):
            break
        else:
            print("Numbers 1 through 4 dumby...")


def __normal_fizz_buzz():

    for i in range(1,101):
        if(i%3 == 0 and i%5 == 0):
            print('\x1b[1;31;0m' + "Fizz Buzz" + '\x1b[0m')
        else:
            if(i%3 == 0):
                print('\x1b[1;31;0m' + "Fizz" + '\x1b[0m')
            elif(i%5 == 0):
                print('\x1b[1;31;0m' + "Buzz" + '\x1b[0m')
            else:
                print(str(i))

def __nm_fizz_buzz():
    n = int(input("Input a low integer: "))
    m = int(input("Input a high integer: "))

    print("Fizz Buzz from " + str(n) + " to " + str(m) + "__________")
    for i in range(n,m+1):
        if(i%3 == 0 and i%5 == 0):
            print('\x1b[1;31;0m' + "Fizz Buzz" + '\x1b[0m')
        else:
            if(i%3 == 0):
                print('\x1b[1;31;0m' + "Fizz" + '\x1b[0m')
            elif(i%5 == 0):
                print('\x1b[1;31;0m' + "Buzz" + '\x1b[0m')
            else:
                print(str(i))
    print("End Fizz Buzz from " + str(n) + " to " + str(m) + "__________")

def __r_fizz_buzz(n,m):
    '''
    so one of the ways to do a no lopp fizz buzz is to use recursion
    ...you could also use an if chain, but that is less pretty

    '''
    if(n < m):

        if (n % 3 == 0 and n % 5 == 0):
            print('\x1b[1;31;0m' + "Fizz Buzz" + '\x1b[0m')
        else:
            if (n % 3 == 0):
                print('\x1b[1;31;0m' + "Fizz" + '\x1b[0m')

            elif (n % 5 == 0):
                print('\x1b[1;31;0m' + "Buzz" + '\x1b[0m')
            else:
                print(str(n))

        __r_fizz_buzz(n + 1, m)


#_____main/testing zone_____
menu()


'''
Notes:
there is no check to see if n or m is larger when user puts it in
user will have to obey the text if they want the script to work

should i add more funny ways to do fizz buzz without a loop?


Testing:
* negetive numbers?


Bugs______________________
None atm




___________________________
'''