"""
Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47
"""

def unique_two_sums(nums, target):
    seen = set()
    count = 0
    pairs = set()

    for num in nums:
        if target - num in seen:
            if (target-num, num) in pairs:
                continue
            else:
                pairs.add((target-num, num))
                count += 1
        else:
            seen.add(num)

    return count

res = unique_two_sums([1, 1], 2)
print(res)