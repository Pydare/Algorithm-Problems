def second_largest(arr):
    first = -999999999
    second = -9999999

    if len(arr) < 2:
        print('Array too small to have 2nd largest item')
    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
    if second == -9999999:
        print('There is no second largest item')
    else:
        return second

print(second_largest([1]))
