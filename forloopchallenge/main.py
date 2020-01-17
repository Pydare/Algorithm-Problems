def bookReading(n,m):
    p = []
    for i in range(1,n+1):
        if i%m == 0:
            if i>9:
                i = int(str(i)[-1])
            p.append(i)
    total = sum(p)
    return(total)
    

q = int(input())
for i in range(q):
    arr = list(map(int,input().split()))
    print(bookReading(arr[0],arr[1]))