def trapDP(height):
    if not height:
        return 0
    ans = 0
    size = len(height)
    left_max, right_max = [0]*size, [0]*size

    left_max[0] = height[0]
    for i in range(1,len(height)):
        left_max[i] = max(height[i],left_max[i-1])
    
    right_max[size-1] = height[size-1]
    for i in range(len(height)-2,-1,-1):
        right_max[i] = max(height[i], right_max[i+1])

    for i in range(1,size):
        ans += min(left_max[i], right_max[i]) - height[i] 
    
    return ans


def trapTwoPointer(height):
    if not height or len(height) == 0:
        return 0
    i, j = 0, len(height) - 1
    lMax, rMax = height[i], height[j]
    res = 0
    while i <= j:
        lMax = max(lMax, height[i])
        rMax = max(rMax, height[j])
        if lMax < rMax:
            res += lMax - height[i]
            i += 1
        else:
            res += rMax - height[j]
            j -= 1
    return res

res = trapTwoPointer([0,1,0,2,1,0,1,3,2,1,2,1])
print(res)
