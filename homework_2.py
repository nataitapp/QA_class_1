__author__ = 'nata'
"""1. Write a function which generates list of N integers in range from x to y
2. Write a function which finds all pairs of elements from the list, whose sum equals a given value"""

import random

def numbers(n, minr, maxr, ):
    l = []
    for i in range(n):
        l.append(random.randint(minr, maxr))
    return l

pick_numbers = numbers(50, 0, 20)
print pick_numbers

def numbers1(l, val):
    res = []
    for i in range(len(l)):
        for j in range(len(l)):
            sum = l[i] + l[j]
            if sum == val:
                res.append((l[i], l[j]))
    return res
    # OR

print numbers1(pick_numbers, 15)
pick_numbers = [5,2]
def numbers2(l, val):
    res = []
    for i in range(len(l)):
        if l.count(val - l[i]) > 0:
            res.append((l[i], val - l[i]))
    return res

print numbers2(pick_numbers, 10)



