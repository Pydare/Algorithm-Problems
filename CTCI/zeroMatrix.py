def reset(arr):
    l = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                l.append((i,j))

    #have to set both rows and columns to 0
    for pts in l:
        #setting the column
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[pts[0]][j] = 0
        #setting the row
        for j in range(len(arr)):
            for k in range(len(arr[j])):
                arr[j][pts[1]] = 0


    return arr
            



arr = [[7,12,55,50],[42,23,40,0],[99,57,9,81],[20,0,93,49]]

r = reset(arr)
print(r)


    