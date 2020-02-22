def moveZeros(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    while count < len(nums):
        nums[count] = 0
        count += 1
    return nums


print(moveZeros([0,1,0,3,12]))


