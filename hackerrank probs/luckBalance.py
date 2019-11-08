def luckBalance(k, contests):
    count = 0
    #swapping elements for easier sorting
    for i in contests:
        i[0],i[1] = i[1],i[0]
    contests.sort()
    first_indices = [i[0] for i in contests] #getting the importace column values
    
    if k < first_indices.count(1):
        second = [i[1] for i in contests[-k:]]
        zeros_sum = [i[1] for i in contests if i[0]==0]
        second = second + zeros_sum
        new_subtract = []
        for i,v in enumerate(contests):
            if contests[i][0]==1 and i<len(contests)-(k) :
                new_subtract.append(contests[i][1])
        
        return sum(second) - sum(new_subtract)
    elif k > first_indices.count(1): #summing everything
        second = [i[1] for i in contests]
        return sum(second)


print(luckBalance(5,[[13,1],[10,1],[9,1],[8,1],[13,1],[12,1],[18,1],[13,1]]))

    
        
            