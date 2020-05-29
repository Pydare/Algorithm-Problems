arr = [[1,3,5,8],[4,2,1,7],[4,3,2,3]]

def minPathCost(arr):
    memo = [[0 for i in range(len(arr[0]))] for _ in range(len(arr))]
    def util(arr,i,j):
        #if the value for cell is already computed, don't compute again
        if memo[i][j] != 0:
            return memo[i][j]
        # at cell (0,0)
        if i == 0 and j == 0:
            memo[i][j] = arr[0][0]
        # if at first row
        elif i == 0:
            memo[i][j] =  util(arr,i,j-1) + arr[0][j]
        elif j == 0:
            memo[i][j] = util(arr,i-1,j) + arr[i][0]
        else:
            x = util(arr,i-1,j)
            y = util(arr,i,j-1)
            memo[i][j] = min(x,y) + arr[i][j]

        return memo[i][j]
    i = len(arr)
    j = len(arr[0])
    res = util(arr,i,j)
    return res

ans = minPathCost(arr)
print(ans)
