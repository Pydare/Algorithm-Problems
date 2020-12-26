# PART I
def maxProfit(prices):
    max_profit = 0
    buy = float('inf')
    
    for i in range(len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] - buy > max_profit:
            max_profit = prices[i] - buy
            
    return max_profit

# PART II
def maxProfit2(prices):
        
    i = 0
    peak, valley = prices[0], prices[0]
    max_profit = 0
    
    while i < len(prices)-1:
        while i < len(prices)-1 and prices[i] >= prices[i+1]:
            i += 1
        valley = prices[i]
        while i < len(prices)-1 and prices[i] <= prices[i+1]:
            i += 1
        peak = prices[i]
        max_profit += peak-valley
        
    return max_profit

# PART III
# https://cs.stackexchange.com/questions/60668/o1-space-on-complexity-algorithm-for-buy-and-sell-stock-twice-interview-que
def maxProfit3(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    t1_cost, t2_cost = float('inf'), float('inf')
    t1_profit, t2_profit = 0, 0

    for price in prices:
        # the maximum profit if only one transaction is allowed
        t1_cost = min(t1_cost, price)
        t1_profit = max(t1_profit, price - t1_cost)
        # reinvest the gained profit in the second transaction
        t2_cost = min(t2_cost, price - t1_profit)
        t2_profit = max(t2_profit, price - t2_cost)

    return t2_profit

# PART IV . TBC LATER
l = [1,2,3,4,5]
for i in range(len(l)-2,-1,-1):
    print(l[i])