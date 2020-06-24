import numpy as np

def uniquePaths(m,n):
    arr = np.zeros((n,m), dtype=np.int32)
    if n==1 or m==1:
        return 1
    for i in range((m)):
        arr[0][i] = 1
    for i in range((n)):
        arr[i][0] = 1
    for i in range(1,n):
        for j in range(1,m):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    return arr[n-1][m-1]

res = uniquePaths(3,3)
print(res)