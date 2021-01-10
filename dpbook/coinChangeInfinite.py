
# coin: coin value, n: no of denominations s: target

def min_coins(coins, target):
    # terminating condition
    if target == 0:
        return 0

    #initialize result
    res = float('inf')
    for i in range(len(coins)):
        #try every coin that has value < s:
        if coins[i] <= target:
            temp = min_coins(coins, target - coins[i])

            res = min(temp + 1, res)

    return res

# cache the results of the above the function
def min_coins_cached(coins, target):
    cache = [float('inf')] * (target + 1)

    def helper(coins, target):
        if target == 0:
            return 0
        if cache[target] != float('inf'):
            return cache[target]
        
        # initialize result
        res = float('inf')
        for i in range(len(coins)):
            if coins[i] <= target:
                temp = helper(coins, target - coins[i])
                
                cache[target] = min(res, temp + 1)

        return cache[target]

    return helper(coins, target)


def min_coins_dp(coin,n,s):
    #result stores minimu no of coins required for s=i, result[s] would have
    #the final result
    result = [float('inf')]*(s+1)
    result[0] = 0

    #compute values bottom-up
    for i in range(1,s):
        #go through all coins < i
        for j in range(n):
            if coin[j] <= i:
                temp = result[i-coin[j]]
                if temp != float('inf') and temp+1 < result[i]:
                    result[i] = temp + 1
    print(result)
    return result[s-1]


ans = min_coins_dp([1,5,6,9],4,11)
print(ans)
