def primeSub(x,y):
    n = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    p = (x-y)
    init = 'NO'
    for i in range(len(n)):
        if p % n[i] == 0:
            init = 'YES'
            return('YES')
            break
        elif p % n[i] != 0:
            init = 'NO'
    if init == 'NO' and init != 'YES':
        return('NO')




q = int(input())
for i in range(q):
    arr = list(map(int,input().split()))
    print(primeSub(arr[0],arr[1]))
    
                
        