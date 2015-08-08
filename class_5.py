__author__ = 'nata'

# string = '{{}}}{{{7483'
#
# def func(s):
#
#     count = 0
#     for i in s:
#         if i == '{':
#             count += 1
#         elif i == '}':
#             if count > 0 :
#                 count -= 1
#             else :
#                 return False
#     if count != 0:
#         return False
#     else :
#         return True
#
# print func(string)

"""fibanacci-print the sequence till n element"""

# list = 5
#
# def nata(n):
#     l = [0]
#     a = 0
#     b = 1
#     for i in range(n):
#         l.append(b)
#         temp = a + b
#         a = b
#         b = temp
#     return l
# print nata(list)

"""print the fibanacci of 5"""

# def jul(n):
#
#     a = 0
#     b = 1
#     for i in range(n-1):
#
#         temp = a + b
#         a = b
#         b = temp
#     return temp
# print jul(temp)

"""fibanacci function"""
def f(n):
    if n == 0 : return 0
    elif n == 1: return 1
    else : return f(n-1) + f(n -2)

print f(10)
# l = []
# for i in range(100):
#     l.append(f(i))
# print l

