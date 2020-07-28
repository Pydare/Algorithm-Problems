"""
a1 >= a2 <= a3 >= a4
[1,2,3,4,5,6,7,8] --> [2,1,4,3,6,5,8,7]

[1,1,1,2,2,3,3,3] -->[1,1,2,1,3,2,3,3] #3 2
   ^
[1,2,4] --> [2,1,0]
"""

def wavy_array(arr):
    n = len(arr)
    res = [0]*n
    arr.sort()

    if not arr:
        return arr
    if len(arr) == 1:
        return arr
    if len(arr) == 2 and arr[0] < arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
        return arr

    for i in range(0,n,2):
        res[i] = arr[i+1]

    for i in range(1,n,2):
        res[i] = arr[i-1]

    return res

sol = wavy_array([40,754,100,9,87,52,12,20]) #754,40,

#print(sol)

#[1,2,3,4,5,6,7,8] --> [2,1,4,3,6,5,8,7]
#[1,2,3,4,5,6,7,8]
def wavy_array_inplace(arr):
    arr.sort()

    for i in range(0,len(arr)-1,2):
        arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr
ans = wavy_array_inplace([1,2,3,4,5,6,7,8,9])
print(ans)

