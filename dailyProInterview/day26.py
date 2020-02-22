def islands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                v = check(grid,i,j)  #checker function
                if v == True:
                    count += 1
    return count

def check(grid,i,j):
    d, flag = {}, False
    if d.get(i, None) is not None:
        d[i] = j
        flag = True
    elif i in d:
        flag = False 
    #checking the immediate surrounding
    if j+1 <= (len(grid[0])):
        if grid[i][j+1] == 1:
            d[i] = j+1
    if i+1 <= (len(grid)):
        if grid[i+1][j] == 1:
            d[i+1] = j
    if i+1 <= (len(grid)) and j+1 <= (len(grid[0])):
        if grid[i+1][j+1] == 1:
            d[i+1] = j+1
    return flag

g = [[1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0]]
print(islands(g))


    
    