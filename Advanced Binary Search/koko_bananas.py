def minEatingSpeed(self, piles, H):
    lo, hi = 1, max(piles)
    
    while lo <= hi:
        K = lo + ((hi - lo) >> 1)
        if self.countTimeEatAllAtSpeed(
                K, piles) <= H:  # count time to eat all bananas at speed K
            hi = K - 1
        else:
            lo = K + 1
    return lo

def countTimeEatAllAtSpeed(self, K, piles):
    countHours = 0  # hours take to eat all bananas
    
    for pile in piles:
        countHours += pile / K
        if pile % K != 0:
            countHours += 1
    return countHours