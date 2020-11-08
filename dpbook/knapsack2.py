"""
Given a knapsack weight W and a set of n items with certain value vali and weight wti, 
we need to calculate the maximum amount that could make up this quantity exactly. 
This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.

Input : W = 8
       val[] = {10, 40, 50, 70}
       wt[]  = {1, 3, 4, 5}       
Output : 110 
We get maximum value with one unit of
weight 5 and one unit of weight 3.
"""

def unbounded_knapsack(W,n,values,weights):
    dp = [0 for _ in range(W+1)]

    # fill the dp using the recursive formula
    for i in range(W+1):
        for j in range(n):
            if weights[j] <= i:
                dp[i] = max(dp[i], values[j] + dp[i-weights[j]])

    return dp[W]