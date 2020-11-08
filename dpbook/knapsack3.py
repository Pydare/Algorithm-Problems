"""
Given weights and values of n items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
In the 0-1 Knapsack problem, we are not allowed to break items. We either take the whole item or don’t take it. 

Input: 
Items as (value, weight) pairs 
arr[] = {{60, 10}, {100, 20}, {120, 30}} 
Knapsack Capacity, W = 50; 

Output: 
Maximum possible value = 240 
by taking items of weight 10 and 20 kg and 2/3 fraction 
of 30 kg. Hence total price will be 60+100+(2/3)(120) = 240
"""

def fractional_knapsack(W,values,weights):
    wei_val = list(zip(values,weights))
    wei_val.sort(key=lambda x: x[0]/x[1], reverse=True)

    total = 0
    for val, wt in wei_val:
        if W-wt >= 0:
            W -= wt
            total += val
        else:
            fraction = W/wt
            total += val * fraction
            W = int(W - (wt*fraction))
            #break
    return total

res = fractional_knapsack(50,[60,100,120],[10,20,30])
print(res)