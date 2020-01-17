def twoSum(nums, target):
    d = {}
    n = []
    for i in range(len(nums)):
        d[i] = nums[i]
    for key, val in d.items():
        if target - val in d.values():
            a = key 
            b = val
            break
    n.append(a)
    n.append(b)
    print(d)
        
twoSum([2, 7, 11, 15], 9)




# def twoSum(nums, target):
#     n = []
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)-1):
#             if target-nums[i] == nums[j]:
#                 a,b = i,j
#                 break
#     n.append(a)
#     n.append(b)
#     print(n)
            

        