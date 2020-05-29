arr = [[0,10,75,94], [-1,0,35,50], [-1,-1,0,80], [-1,-1,-1,0]]
memo = [[0 for i in range(len(arr[0]))] for _ in range(len(arr))]

def calculateMinCost(arr,s,d):
    if s==d or s==d-1:
        return arr[s][d]

    if memo[s][d] == 0:
        minCost = arr[s][d]
        #try every intermediate station to find min
        for i in range(s+1,d):
            #min cost of going from s to i and min cost of going from i to d
            temp = calculateMinCost(arr,s,i) + calculateMinCost(arr,i,d)

            if temp < minCost:
                minCost = temp

        #store the minCost in cache
        memo[s][d] = minCost

    return memo[s][d]


res = calculateMinCost(arr,0,len(arr)-1)
#print(res)


#bottom up approach for dynamic programming
def calculateMinCost2(cost):
    #minCost[i] = min cost from station 0 to station i
    minCost = [0] * len(cost[0])
    minCost[1] = cost[0][1]

    for i in range(2,len(cost)):
        minCost[i] = cost[0][i]
        for j in range(1,i):
            if minCost[i] > minCost[j] + cost[j][i]:
                minCost[i] = minCost[j] + cost[j][i]
    return minCost[len(cost)-1]

res2 = calculateMinCost2(arr)
print(res2)