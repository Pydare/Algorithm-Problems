def min_coins(coins,target):
    n = len(coins)

    res = [[0 for _ in range(target+1)] for _ in range(n+1)]

    for i in range(target+1):
        res[0][i] = i
    
    for i in range(1,n):
        for j in range(1,target+1):
            if j >= coins[i]:
                res[i][j] = min(res[i-1][j], res[i][j-coins[i]]+1)
            else:
                res[i][j] = res[i-1][j]

    return res[n-1][target]

ans = min_coins([1,2,3], 9)
print(ans)

