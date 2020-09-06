"""
Input : k = 2, A = {10, 20, 30, 40} 
Output : 60.
Here we can divide first 3 boards for
one painter and the last board for 
second painter.
"""
import sys
def minimum_time(A,k):
    n = len(A)
    lo, hi = max(A), sum(A)
    res = sys.maxsize

    #edge case
    if len(A) < k:
        return -1

    while lo < hi:
        mid = (lo+hi)//2
        if is_possible(A,n,k,mid):
            res = min(res,mid)
            hi = mid
        else:
            lo = mid+1
    return res

def is_possible(A,n,k,mid):
    curr_painters = 1
    curr_time = 0

    for i in range(n):
        if curr_time + A[i] > mid:
            curr_painters += 1
            curr_time = A[i]
            if curr_painters > k:
                return False
        else:
            curr_time += A[i]
    return True

res = minimum_time([250, 74, 159, 181, 23, 45, 129, 174],6)
print(res)