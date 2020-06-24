def combinationSum(candidates,target):
    ret = []

    def helper(curr,left,si):
        if left == 0:
            ret.append(curr+[])
            return
        
        for i in range(si,len(candidates)-1):
            if left - candidates[i] >= 0:
                curr.append(candidates[i])
                helper(curr,left-candidates[i],i+1)
                curr.pop()
    helper([],target,0)
    return ret


def combinationSum2(candidates,target):
    res = []

    if not candidates  or len(candidates)==0:
        return res

    candidates.sort()
    combination =  []
    findCombination(res, combination, candidates, target, 0)

    return res

def findCombination(res,combination,candidates,target,start):
    if target==0:
        res.append(combination+[])
        return
    for i in range(start,len(candidates)):
        if candidates[i] > target:
            break
        combination.append(candidates[i])
        findCombination(res,combination,candidates, target-candidates[i],i)
        combination.pop()





res = combinationSum([10,1,2,7,6,1,5],8)
print(res) 