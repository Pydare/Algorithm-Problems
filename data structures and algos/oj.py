def summer_69(a):
    s = 0
    b = []
    for i in a:
        if i >= 6 and i <= 9:
            b.append(i)
        if i not in b:
            s += i
    print(s)
         

summer_69([4,5,6,7,8,9,10,11])

