def get_min(a,b):
    return a if a>b else b

def min_path_cost(cost,m,n):
    #base case
    if m==0 and n==0:
        return cost[0][0]
    if m==0:
        return min_path_cost(cost,m,n-1) + cost[0][n]
    if n==0:
        return min_path_cost(cost,m-1,n) + cost[m][0]

    x = min_path_cost(cost,m-1,n)
    y = min_path_cost(cost,m,n-1)
    return get_min(x,y) + cost[m][n]