import sys

#coin: coin value, n: no of denominations s: target

def min_coins(coin,n,s):
    #terminating condition
    if s == 0:
        return 0

    #initialize result
    res = sys.maxsize
    for i in range(n):
        #try every coin that has value < s:
        if coin[i] <= s:
            temp = min_coins(coin,n,s-coin[i])

            res = min(temp+1,res)

    return res

def min_coins_dp(coin,n,s):
    #result stores minimu no of coins required for s=i, result[s] would have
    #the final result
    result = [sys.maxsize]*(s+1)
    result[0] = 0

    #compute values bottom-up
    for i in range(1,s):
        #go through all coins < i
        for j in range(n):
            if coin[j] <= i:
                temp = result[i-coin[j]]
                if temp != sys.maxsize and temp+1 < result[i]:
                    result[i] = temp + 1
    print(result)
    return result[s-1]


ans = min_coins_dp([1,5,6,9],4,11)
print(ans)
