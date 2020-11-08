"""
10,9,2,5,3,7,101,18
         ^
1 ,1,1,2,2,2,1,1
"""
def lic(nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i < j:
            m = (i + j) // 2
            if x > tails[m]:
                i = m + 1
            else:
                j = m
        tails[i] = x
        print(tails)
        size = max(i + 1, size)
    return size

ans = lic([10,9,2,5,3,7,101,18])
print(ans)