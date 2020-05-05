def sort_partially_sorted(nums, k):
    front,back = 0,0
    for i in range(len(nums)):
        front = i+1
        front_end = front+2
        while front <= front_end and front <= len(nums)-1:
            if nums[front] < nums[i]:
                nums[i], nums[front] = nums[front], nums[i]
            front += 1
        back = i-1
        back_end = back-2
        while back >= back_end and back > 0:
            if nums[back] > nums[i]:
                nums[back],nums[i] = nums[i], nums[back]
            back -= 1
    return nums 

r = sort_partially_sorted([3, 2, 6, 5, 4], 2)
print(r)