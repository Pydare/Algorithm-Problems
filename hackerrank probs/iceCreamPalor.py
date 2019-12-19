def whatFlavors(cost, money):
    d,l = {},[]
    for i in range(len(cost)):
        d[cost[i]] = i
    for i,v in enumerate(cost):
        a = v
        diff = money - a
        if diff in d.keys() and d[diff] != i:
            l.append(i+1)
            l.append(d[diff]+1)
            break
    for i in l:
        print(i,end=' ')


whatFlavors([1,4,5,3,2], 4)