def maxDistToClosest(seats): #O(n) space
    N = len(seats)
    left, right = [N] * N, [N] * N

    for i in range(N):
        if seats[i] == 1: left[i] = 0
        elif i > 0: left[i] = left[i-1] + 1

    for i in range(N-1, -1, -1):
        if seats[i] == 1: right[i] = 0
        elif i < N-1: right[i] = right[i+1] + 1

    return max(min(left[i], right[i])
        for i, seat in enumerate(seats) if not seat)

import itertools
def maxDistToClosest2( seats): # O(1) space
        ans = seats.index(1)
        seats.reverse()
        ans = max(ans,seats.index(1))
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K+1)/2)

        return ans

a = [1,2,3]
b = [5,6,7]
