###bidirectional DP solution

def max_profit(prices):
    if len(prices) <= 1:
        return 0

    left_min = prices[0]
    right_max = prices[-1]

    length = len(prices)
    left_profits = [0] * length
    right_profits = [0] * (length+1)

    for l in range(1,length):
        left_profits[l] = max(left_profits[l-1],prices[l]-left_min)
        left_min = min(left_min,prices[l])

        r = length-1 - l
        right_profits[r] = max(right_profits[r+1], right_max-prices[r])
        right_max = max(right_max,prices[r])

    max_profit = 0
    for i in range(0,length):
        max_profit = max(max_profit, left_profits[i] + right_profits[i+1])
    
    return max_profit

##One pass solution
import sys
def max_profit2(prices):

    t1cost, t2cost = sys.maxsize, sys.maxsize
    t1profit, t2profit = 0, 0

    """
    [3,3,5,0,0,3,1,4]
    a = 3
    b = 0
    c = 3
    d = 3
    """

    for price in prices:
        #the maximum profit if only one transaction is allowed
        t1cost = min(t1cost,price)
        t1profit = max(t1profit, price-t1cost)
        #reinvest the gained profit in the second transaction
        t2cost = min(t2cost, price-t1profit)
        t2profit = max(t2profit, price-t2profit)

    return t2profit