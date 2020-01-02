def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    for i, val in enumerate(arr):
        temp[val] = i
        pos += 1
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]




print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))