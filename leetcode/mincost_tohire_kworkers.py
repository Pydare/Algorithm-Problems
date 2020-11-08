import itertools
def mincostToHireWorkers(quality,wage):

    res, n = float('inf'), len(wage)
    
    for i in range(n):
        #get the ratio for the ith index
        temp = []
        for j in range(n):
            temp.append(quality[j]/quality[i])
        
        #get the cost of each worker using this ratio
        temp = [wage[i]*x for x in temp]
        
        #get all possible k combinations
        for comb in itertools.combinations(enumerate(temp),K):
            #check if each cost is less than wage
            for idx,el in comb:
                if wage[idx] > el:
                    break
            
            temp_sum = sum(x[1] for x in comb)
            res = min(res, temp_sum)
                
    return res