__author__ = 'nata'
l = []
for x in range(1,10):
    l.append(str(x))
l_1 =''.join(l)
print l_1
for i in l_1:
    k = int(i) * 2
    print k
