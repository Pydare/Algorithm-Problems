def thanos(arr):
    temp = []
    while arr != sorted(arr):
        half = (len(arr)//2)
        end = len(arr) 

        a = arr[0:half]
        b = arr[half:end]

        if sorted(a)[0] == a[0] and sorted(a)[half//2] == a[half//2] and sorted(a)[half-1] == a[half-1]:
            temp = a
        elif sorted(b)[0] == b[0] and sorted(b)[half//2] == b[half//2] and sorted(b)[half-1] == b[half-1]:
            temp = b
        arr = temp
    return(len(arr))


q = int(input())
arr = list(map(int,input().split()))
print(thanos(arr))




# 78 16 40 90 4 13 99 19 | 41 47 50 68 71 79 96 76