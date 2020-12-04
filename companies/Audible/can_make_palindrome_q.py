def canMakePaliQueries(s, queries):
    N = 26
    S = len(s) + 1
    ints = list(map(lambda c: ord(c) - ord('a'), s))

    dp = [0] * S
    for i in range(1, S):
        dp[i] = dp[i-1] ^ (1 << ints[i-1])

    ones = lambda x: bin(x).count('1')
    return [
        ones(dp[r+1] ^ dp[l]) >> 1 <= k
        for l, r, k in queries
    ]
