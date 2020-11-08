"""
minimum number of coins to form a target
eg. target=5, coins=1,2,3
"""

def min_coins_top_dow(total,coins,map_):
    #if total is 0, nothing to do, return 0
    if total == 0:
        return 0

    #if map contains the result means we calculated it before
    if total in map_:
        return map_[total]

    #iterate through all coins and see which one gives best result
    min_val = float('inf')
    for i in range(0,len(coins)):
        #if value of coin is greater than total we are looking for, continue
        if coins[i] > total:
            continue

        #recursive with total - coins[i] as new total
        val = min_coins_top_dow(total-coins[i],coins,map_)

        #if val we get from picking coins[i] is less than value found so far
        if val < min_val:
            min_val = val

    #if min val doesn't change. leave it as it was
    min_val = min_val+1 if min_val!=float('inf') else float('inf')

    #memoize the minimum for current total
    map_[total] = min_val
    return min_val
map_ = [0]*11
res = min_coins_top_dow(10,[3,5,2],map_)
print(res)


"""

"""
def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in coins:
        for j in range(1, amount + 1):
            if j >= i:
                dp[j] += dp[j - i]
    return dp[amount]