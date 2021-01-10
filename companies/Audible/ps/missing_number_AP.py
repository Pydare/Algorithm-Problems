def missingNumber(arr):
        
    return (arr[0] + arr[-1]) * (len(arr) + 1) // 2 - sum(arr)

# O(logN) soln
def missingNumber2(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    n = len(arr)
    diff = (arr[-1] - arr[0]) // n
    lo, hi = 0, n
    while lo < hi: # 5,7,11,13
        mid = (lo + hi) >> 1 # or lo+hi//2
        if arr[mid] == arr[0] + (mid * diff):
            lo = mid + 1
        else:
            hi = mid
    return arr[0] + (lo * diff)