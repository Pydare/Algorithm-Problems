def first_misising_integer(nums):
    smallest = min(i for i in nums if i > 0)
    while True:
        smallest += 1
        if smallest not in nums:
            break
    return smallest
            


print(first_misising_integer([3, 4, -1, 1]))
             