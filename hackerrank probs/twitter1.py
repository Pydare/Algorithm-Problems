from itertools import chain
def kDifference(a, k):
    d,l = {},[]
    sub = [abs(i-k) for i in a]
    for i in range(len(sub)):
        d[sub[i]] = sub[i]+k
    for key,v in d.items():
        if key in a :
            l.append((key,v))
            
    print((len(l)))



kDifference([2,4,6,8,10,12],2)