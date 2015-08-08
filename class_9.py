__author__ = 'nata'

# still biggest value in the house---------------homework-------------------------

# def find_hit():
#
#
#
# def make_hit(j, l):
#     if j == 0:
#     elif == len()
#     else

#---------------------------------------------------------------------

"""find same count of letters in 2 words HANNAH ANNA"""

n = 'hannah'
n1 = 'anna'

d = dict()
for elem in n:
    if elem not in d:
        d[elem]=1
    else:
        d[elem] += 1

for i in n1:
    if i in d and d[elem] > 0:
        d[elem] -=1
        print elem