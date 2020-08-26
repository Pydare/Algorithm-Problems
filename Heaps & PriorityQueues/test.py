def search(matrix):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if reach_atlantic(matrix,i,j):
                res.append([i,j])
    return res

def reach_pacific(matrix,i,j):
    if i == 0 or j == 0:
        return True
    
    if i-1 >= 0 and matrix[i-1][j] <= matrix[i][j]:
        res = reach_pacific(matrix,i-1,j)
    elif j-1 >= 0 and matrix[i][j-1] <= matrix[i][j]:
        res = reach_pacific(matrix,i,j-1)
    else:
        return False

    return res

def reach_atlantic(matrix,i,j):
    if i == len(matrix)-1 or j == len(matrix[0])-1:
        return True
    
    if i+1 < len(matrix) and matrix[i+1][j] <= matrix[i][j]:
        res = reach_atlantic(matrix,i+1,j)
    elif j+1 < len(matrix[0]) and matrix[i][j+1] <= matrix[i][j]:
        res = reach_atlantic(matrix,i,j+1)
    elif j-1 >= 0 and matrix[i][j-1] <= matrix[i][j]:
        res = reach_atlantic(matrix,i,j-1)
    else:
        return False
    return res

matrix = [[10,10,10],[10,1,10],[10,10,10]]
ans = search(matrix)
print(ans)