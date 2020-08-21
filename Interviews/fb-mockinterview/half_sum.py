def can_partition(nums):
    s = sum(nums)
    if s%2 != 0: return False

    return can_find_sum(nums, s//2, 0, len(nums), {})

def can_find_sum(nums,target,ind,n,d):
    if target in d: return d[target]
    if target == 0: d[target] = True
    else:
        d[target] = False
        if target > 0:
            for i in range(ind, n):
                if can_find_sum(nums, target-nums[i], i+1, n, d):
                    d[target] = True
                    break
    return d[target]