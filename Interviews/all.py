def pairs(arr,target):
    d,l = {},[]
    for i in range(len(target)):
        d[target[i]] = i
    for k,v in enumerate(target):
        a = v
        diff = target - a
        if a in d.keys():
            l.append[]