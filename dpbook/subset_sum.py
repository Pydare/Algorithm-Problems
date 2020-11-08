def is_subset_sum(arr,n,x):
    if x == 0:
        return True

    if n == 0:
        return False
    
    #if first element is > x, ignore it
    if arr[0] > x:
        return is_subset_sum(arr[1:],n-1,x)

    #else check both ways, excluding first element in the sum
    #including first element in the sum
    return is_subset_sum(arr[1:],n-1,x) or is_subset_sum(arr[1:],n-1,x-arr[0])

res = is_subset_sum([3,2,7,1],4,6)
print(res)

def is_subset_sum_dp(arr,n,x):
    
    mat = [[False for _ in range(x+1)] for _ in range(n)]

    #if x is 0, then the answer is true
    for i in range(len(mat)):
        mat[i][0] = True
    
    #if x is not 0 and arr is empty answer is false
    for j in range(len(mat[0])):
        mat[0][j] = True if j==arr[i] else False 

    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            if mat[i-1][j-1] == True:
                mat[i][j] = True
            else:
                mat[i][j] = mat[i-1][j-arr[i-1]]

    return mat[n-1][x]
res2 = is_subset_sum_dp([3,2,7,1],4,6)
print(res2)

    