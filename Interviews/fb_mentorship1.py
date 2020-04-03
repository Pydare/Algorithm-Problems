def wrongPosition(arr):
    arr_sort = arr.copy()
    arr_sort.sort()
    count = 0
    for i in range(len(arr)):
        if arr[i] != arr_sort[i]:
            count += 1
    return count

r = wrongPosition([1,1,3,3,4,1])
print(r)
