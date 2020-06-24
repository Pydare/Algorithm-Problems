def jump(nums):
    n = len(nums)
    if n < 2:
        return 0

    #max position one could reach starting from index <= i
    max_pos = nums[0]

    #max number of steps one could do inside this jump
    max_steps = nums[0]

    jumps = 1
    for i in range(1,n):
        #if to reach this point one needs one more jump
        if max_steps < i:
            jumps += 1
            max_steps = max_pos
        max_pos = max(max_pos, nums[i]+1)

    return jumps
