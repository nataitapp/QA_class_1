__author__ = 'nata'


l = range(1,11)
l_1 =[]

for elem in l:
#for i in range(len(l)):
    temp = elem * 2
#   temp = l[i] * 2
    l_1.append(temp)

l_1.reverse()

while 4 in l_1:
    l_1.remove(4)

del l_1[3]
l_1.sort()
l_1.append('Nata')
print l_1










