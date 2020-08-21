def findHighPoints(elevations):

    #length of rows and columns
    n, m = len(elevations), len(elevations[0])

    # initializing the high points variable
    high_points = [[False for _ in range(m)] for _ in range(n)]

    #initializing the directions variable
    #right,left,down,up,NW,SE,NE,SW
    directions = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)] 
    for i in range(n):
        for j in range(m):
            flag = False
            high = (i,j)
            for dirr in directions:
                x,y = i+dirr[0], j+dirr[1]
                if 0 <= x < n and 0 <= y < m and elevations[x][y] >= elevations[high[0]][high[1]]:
                    flag = True
                    break
            # no higher surrounding
            if not flag:
                high_points[high[0]][high[1]] = True
                        
    #return highPoints
    return high_points