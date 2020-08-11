"""
[1,1,1,5,2,3,4,1,6,2,3], k = 6
"""
def subarray(nums,k):
    i,j,count = 0,0,0

    while j < len(nums):
        temp = nums[i:j]
        if sum(temp) == k:
            count += 1 
        if sum(temp) < k:
            j += 1
        elif sum(temp) > k:
            i += 1

    return count

nums = [1,1,1,5,2,3,4,1,6,2,3]
res = subarray(nums,6)
print(res)