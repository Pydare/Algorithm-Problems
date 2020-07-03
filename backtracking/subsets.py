"""
[1,2,2] ---> [],[1],[2],[1,2],[2,2], [1,2,2]
"""

def subset_duplicates(nums):
    nums.sort()
    res = []
    def helper(nums,res,temp,idx):
        res.append(temp)                                #res = [[],[1],[1,2],[1,2,2],[2]]

        for i in range(idx,len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            else:
                helper(nums, res, temp+[nums[i]], i+1)        # idx=2  temp=[1,2]  i=1

    helper(nums,res,[],0)
    return res


ans = subset_duplicates([1,2,2])
print(ans)