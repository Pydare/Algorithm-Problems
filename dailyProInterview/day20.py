def witnesses(height):
    count, flag = 0, height[-1]
    for i in range(len(height)-1,-1,-1):
        if height[i] >=  flag:
            count += 1
            flag = height[i]
    return count


print(witnesses([3,6,3,4,1]))