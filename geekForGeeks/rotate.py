def leftRotate(arr,n):
    l = len(arr)
    for i in range(len(arr)):
        arr[i] = arr[i + (n%l)]
    return arr

arr = [1,2,3,4,5,6,7]

res = leftRotate(arr,2)
print(res)





arr2 = [3,4,5,6,7,1,2]