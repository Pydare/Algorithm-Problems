def shuffle(nums,n):
    
    get_desired_idx = lambda i: i*2 if i<n else (i-n)*2+1
    for i in range(2*n):
        j=i
        while nums[i] >= 0:
            j = get_desired_idx(j)
            nums[i],nums[j] = nums[j],-nums[i]
            print(nums)
    for i in range(2*n):
        nums[i] = -nums[i]
    return nums

res = shuffle([2,5,1,3,4,7],3)
print(res)