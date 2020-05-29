def bubblesort(arr,n):
    #perform one pass
    for i in range(n):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    bubblesort(arr,n-1)
    #return arr

arr = [7,3,1,2,9,4,6]
n = len(arr)-1
bubblesort(arr,n)
print(arr)


