def processingTime(arr):
    sum_ = sum(arr)
    target = sum_//2
    d = dict()
    for i in range(len(arr)):
        d[target - arr[i]] = arr[i]
    count = 0
    for i in arr:
        if i in d:
            count += 1
    if count == len(arr):
        return True
    else:
        return False


print(processingTime([1,2,5,3]))