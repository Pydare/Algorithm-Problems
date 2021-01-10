"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. 
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this 
subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).

values=[120,100,60]
weight=[10,20,30]
W=50

example: W=6, values=[10,15,40], weights=[1,2,3]

   0   1   2   3   4   5   6

0  0   0   0   0   0   0   0

1  0  10  10  10  10  10  10

2  0  10  15  25  25  25  25

3  0  10  15  40  50  55  65
"""

# recursive solution
def maximum_values(values, weights, W, n):
    
    # base case
    if n == 0 or W == 0:
        return 0
    
    # If weight of the nth item is 
    # more than Knapsack of capacity W, 
    # then this item cannot be included 
    # in the optimal solution
    if weights[n-1] > W:
        return maximum_values(values, weights, W, n-1) # skipping that weight

    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included
    else:
        return max(values[n-1] + maximum_values(values, weights, W-weights[n-1], n-1), maximum_values(values, weights, W, n-1))



# memoized solution of the recursive solution

def max_values_memo(values, weights, W, n):
    memo = [[-1 for _ in range(W+1)] for _ in range(n+1)]

    def helper(values, weights, W, n):
        # base case
        if n == 0 or W == 0:
            return 0
        if memo[n][W] != -1:
            return memo[n][W]

        if weights[n-1] > W:
            memo[n][W] = helper(values, weights, W, n-1)
            return memo[n][W]
        else:
            memo[n][W] = max(values[n-1] + helper(values, weights, W-weights[n-1], n-1), helper(values, weights, W, n-1))
            return memo[n][W]

    return helper(values, weights, W, n)


# dp solution
def max_values_dp(values, weights, W):

    dp = [[0 for _ in range(W + 1)] for _ in range(len(weights) + 1)]
    m, n = len(dp), len(dp[0])

    for i in range(1, m):
        for j in range(1, n):
            if j < weights[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(values[i-1] + dp[i-1][j-weights[i-1]], dp[i-1][j])

    return dp[m-1][n-1]

ans = max_values_dp([10,15,40],[1,2,3],6)
print(ans)