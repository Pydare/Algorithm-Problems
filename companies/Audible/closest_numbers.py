from collections import defaultdict
def closest(nums):
    nums.sort()
    d = defaultdict(list)

    for i in range(1, len(nums)):
        d[nums[i] - nums[i-1]].append([nums[i-1], nums[i]])

    return d[min(d)]

ans = closest([1,2,3,4])
print(ans)