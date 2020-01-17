import math
def sortThisNigga(arr):
    mas = []
    t = 1
    lenght = 1
    for i in range(int(math.log(len(arr))/math.log(2))):
        t *= 2
        for j in range(len(arr)//t):
            start = j*t
            stop = j*t+t
            mas.append(arr[start:stop])

    for e in mas:
        if e == sorted(e):
            if len(e) > lenght:
                lenght = len(e)
        return lenght

n = int(input())
arr = list(map(int,input().split()))
print(sortThisNigga(arr))