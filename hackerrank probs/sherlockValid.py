def isValid(s):
    distinctList = []
    countList = []
    for c in s:
        if c not in distinctList:
            distinctList.append(c)
    for d in distinctList:
        count = s.count(d)
        countList.append(count)
    #print(countList)
    key = countList[0]
    flags = 0
    for count in countList:
        if(key != count):
            flags+=1
    if(flags > 1):
        print("NO")
    else:
        print("YES")
    print(countList)


isValid('aabb')
     
