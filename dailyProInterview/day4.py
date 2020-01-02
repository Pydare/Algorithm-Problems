def getRange(arr, target):
    l = []
    for i,val in enumerate(arr):
        if val == target:
            l.append(i)
    if len(l) == 0:
        l.append(-1)
        l.append(-1)
    else:
        l = [l[0],l[-1]]
    
    return l

print(getRange([1,2,3,4,5,6,10],9))
