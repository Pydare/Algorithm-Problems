arr = [1,2,3,4,5,6]

def update(arr,i):
    if i == len(arr):
        return
    arr[i] += arr[i-1]
    update(arr,i+1)
    return arr

ans = update(arr,1)
print(arr)