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
    # for l = [1, 2, 1, 2], should I return [1, 2] twice or only once ? should I return [2, 1] as well?

print numbers1(pick_numbers, 15)



