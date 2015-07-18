__author__ = 'nata'
""" generate 4 digit number"""

import random

def x():
    s = ''
    for i in range(4):
        s = s + str(random.randint(0, 9))
    return s
y = x()
print y

def numbers():
    cow = 0
    bull = 0

    user = raw_input('enter 4 digit number:')
    for i in range(len(user)):
        if user[i] == y[i]:
            bull = bull + 1
        elif user[i] in y :
            cow = cow + 1
    return cow, bull

cow, bull = numbers()

print cow, bull


""" count factorial"""

# def fact(x):
#     result=1
#     if x < 2:
#         return 1
#     for i in range(2, x + 1):
#         result = result * i
#     return result
# z = fact(5)
# print z

"""repetative/arithmetical progression"""

# def arif(start, end, step):
#     l = []
#     temp = start
#     for i in range(end):
#         l.append(temp)
#         temp = temp + step
#     return l
# print l


"""distance 10"""


# def val(distance, jump):
#     if distance % jump == 0 :
#         return distance / jump
#     else :
#         return (distance/jump) + 1
# z = val(10, 3)
# print z






































