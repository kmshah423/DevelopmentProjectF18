# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 14:52:25 2018

@author: CuddlyLicky
"""

print("Enter starting number")
n = int(input())

print("Enter ending number")
m = int(input())


def recursive(first):
    if (first < m):
        print(first)
        if (first % 3 == 0):
            print("Bizz")
        if (first % 5 == 0):
            print("Fuzz")
        recursive(first + 1)
    return

recursive(n)

