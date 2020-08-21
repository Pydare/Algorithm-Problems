from collections import defaultdict

def floodfill(altitude):
    n = len(altitude)

    #step 0: point each cell to its lowest cell neigbor if no surrounding neighbor is smaller, point to itself

    #directions for down, up, right and left
    directions = [(1,0),(-1,0),(0,1),(0,-1)] 

    #outdegree keeps track of each cell and the lower cell it points to
    outdegree = defaultdict()

    #get all the outdegree values
    for i in range(n):
        for j in range(n):
            #check the 4 directions for the least value ie sink
            #initialize sink to the cell itself
            sink = (i,j)
            for dirr in directions:
                x,y = i+dirr[0], j+dirr[1]
                if 0 <= x < n and 0 <= y < n and altitude[x][y] < altitude[sink[0]][sink[1]]:
                    sink = (x,y)
            #map their directions
            outdegree[(i,j)] = sink

    #step 1: get their indegree values ie each cell with all the cells pointing towards it
    indegree = {}
    for i in range(n):
        for j in range(n):
            indegree[(i,j)] = []
    for k,v in outdegree.items():
        indegree[v].append(k)
    #remove itself from list of indegrees eg remove (0,0) from the values of (0,0)
    for m,n in indegree.items():
        for vals in n:
            if vals == m:
                indegree[m].remove(vals)

    #dfs function to search indegree
    def dfs(nei):
        if nei and nei not in seen:
            seen.append(nei)
            for nei in indegree[nei]:
                dfs(nei)

    #step 2: outdegree equal key,value pairs show that such key is a basin
    res = []
    for key, val in outdegree.items():
        if key == val:
            #run a dfs on the vals of the indegree and keep counting
            #seen keeps count of all the cells connected to each other
            seen = [key]
            for nei in indegree[key]:   #seen [1,2,4,3,6]
                dfs(nei)
            res.append(len(seen))

    return res

#altitude = [[1, 5, 2],[2, 4, 7],[3, 6, 9]]
altitude = [[1, 0, 2, 5, 8], [2, 3, 4, 7, 9], [3, 5, 7, 8, 9], [1, 2, 5, 4, 3], [3, 3, 5, 2, 1]]
ans = floodfill(altitude)
print(ans)



    

