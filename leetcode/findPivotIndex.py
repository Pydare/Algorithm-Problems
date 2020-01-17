def pivotInex(nums):
    com = {}
    c = nums[0]
    com[c] = 0
    for i in range(1,len(nums)):
        c = nums[i] + c
        com[c] = i
    d = nums[len(nums)-1]
    for i in range(len(nums)-1,0,-1):
        if d in com.keys():
            return com[d]+1
        else:
            d = nums[i] + d
    


    

print(pivotInex([1, 7, 3, 6, 5, 6]))
        
