import numpy as np
def uniqueII(obstacle):
    m = len(obstacle)
    n = len(obstacle[0])
    for i in range((m)):
        obstacle[0][i] = 1
    for i in range((n)):
        obstacle[i][0] = 1
    for i in range(1,n):
        for j in range(1,m):
            if obstacle[i-1][j]==1 and i!=0:
                obstacle[i][j] = obstacle[i][j-1]
            elif obstacle[i][j-1]==1 and j!=0:
                obstacle[i][j] = obstacle[i-1][j]
            else: 
                obstacle[i][j] = obstacle[i-1][j] + obstacle[i][j-1]
    return obstacle[n-1][m-1]

tester = [
         [0,0,0],
         [0,1,0],
         [0,0,0]
         ]
print(uniqueII(tester))


    