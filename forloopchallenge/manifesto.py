#TEST CASES
#if the 3rd is greater than 2nd and less than the 1st
#if the 3rd is greater than 2nd and greater than the 1st
#if the 3rd is less than the 2nd and greater than the 1st
#if the 3rd is less than the 2nd and less thanthe 1st


def nextPermutation(nums):
    if nums[2] > nums[1] and nums[2] < nums[0]:
        nums[2],nums[1] = nums[1],nums[2]
    if nums[2] > nums[1] and nums[2] > nums[0]:
        nums[2],nums[1]  = nums[1],nums[2]
    if nums[2] < nums[1] and nums[2] > nums[0]:
        nums[2],nums[1] = nums[1],nums[2]
        nums[0],nums[1] = nums[1],nums[0]
    if nums[2] < nums[1] and nums[2] < nums[0]:
        nums.reverse()
    print(nums)


nextPermutation([3,1,2])


