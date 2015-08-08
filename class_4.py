__author__ = 'nata'

d = dict(zip(['Name', 'Age', 'Sex'], ['Stan', '35', 'M']))
print d


"""find unique elements in dictionary"""

def func(val) :
    d = dict() dict ={}
    for i in val :
       if i not in d :
           d[i] = 1
       else :
           del d[i]
    return d.keys()

"""most used character in the string"""

def func(val) :
    temp = 0
    char = ''
    d = dict() dict ={}
    for i in val :
       if i not in d :
           d[i] = 1
       else :
           d[i] += 1
    for k in d :
        if d[k] > temp :
            temp = d[k]
            char = k
    print char, temp


"""buble sort"""

val = [4,6,2,4,8]
i = 0
for i in range(len(val)) :
    for k in range(len(val)-i):
        if val[k] > val [k+1]:
            temp =val[k]
            val[k] = val[k+1]
            val[k+1] = temp

 ## SAME WAY WITH WHILE LOOP

val = [4,6,2,4,8]
flag = True
while True:
    flag = False
        for k in range(len(val)-i):
        if val[k] > val [k+1]:
            temp =val[k]
            val[k] = val[k+1]
            val[k+1] = temp






















