def countWays(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return countWays(n-1) + countWays(n-2)