def sortNums(nums):
    a = min(nums)
    b = max(nums)
    one_i,three_i = 0,len(nums)-1
    check = 0
    while check <= three_i:
        if nums[check] == a:
            nums[check], nums[one_i] = nums[one_i], nums[check]
            check += 1
            one_i += 1
        elif nums[check] != a and nums[check] !=b:
            check +=1
        elif nums[check] == b:
            nums[check], nums[three_i] = nums[three_i], nums[check]
            three_i -= 1
    return nums

print(sortNums([3,3,2,1,3,2,1]))
