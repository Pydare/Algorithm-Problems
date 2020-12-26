def maxDistToClosest(seats):
        
    people = (i for i, seat in enumerate(seats) if seat) # (0,4,6)
    prev, future = None, next(people)
    
    ans = 0
    for i, seat in enumerate(seat):
        if seat:
            prev = i
        else:
            while future is not None and future < i:
                future = next(people, None)
                
            left = float('inf') if prev is None else i - prev
            right = float('inf') if future is None else future - i
            ans = max(ans, min(left, right))
            
    return ans

import itertools
def maxDistToClosest2( seats):
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
