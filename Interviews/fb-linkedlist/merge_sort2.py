def merge(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left, right = merge(arr[:mid]), merge(arr[mid:])
        m,n = len(left), len(right)
        i = j = k = 0

        while i<m and j<n:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i<m:
            arr[k] = left[i]
            i+=1
            k+=1
        while j<n:
            arr[k]=right[j]
            j+=1
            k+=1

    return arr

arr = [5,3,4,1,2,10,50,6,9,43,52,7,55,100,90]
res = merge(arr)
print(res)


#################################################################
from itertools import product
m,n = 4,5
borders = list(product(range(m),[0,n-1])) + list(product([0,m-1],range(n)))
print(borders)