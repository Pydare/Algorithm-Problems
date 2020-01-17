def findMin(arr):
    if len(arr) < 1:
        print('Invalid input')
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return min(ar)
    return smallestUtils(arr,0,len(arr)-1)

def smallestUtils(arr,start,stop):
    mid = (start + stop)//2
    if arr[mid] > arr[start]:
        