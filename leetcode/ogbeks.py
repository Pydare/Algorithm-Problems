def change(n):
    #base case
    if n == 0:
        return
    l = []
    a,b = 5,7
    if n < a:
        n += a
        n += a
        a = b  
        change(n-a)
        l.append(a)
    else:
        change(n-a)
        l.append(a)
    return l


print(change(24))
    
    