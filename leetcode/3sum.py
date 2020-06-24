def duplicates(nums):
    count = 1
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[count] = nums[i+1]
            count += 1

    temp = len(nums)-count
    for i in range(temp):
        nums.pop()
    return nums


res = duplicates([0,0,1,1,1,2,2,3,3,4])
print(res) 