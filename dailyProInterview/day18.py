def removeConsecutiveSumTo0(l):
    indices = []
    for i in range(len(l)):
        summer = l[i]
        for j in range(i+1,len(l)):
            summer += l[j]
            if summer == 0:
                indices.append((i,j))
                break        
    return indices 

print(removeConsecutiveSumTo0([10,5,-3,-3,1,4,-4]))

Given a  list of integers, remove all consecutive nodes that sum up to 0.
Input: [10,5,-3,-3,1,4,4]
Output: 10
