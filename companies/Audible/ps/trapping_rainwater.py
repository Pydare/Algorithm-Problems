# FIRST SOLUTION
def trap(height):
    if not height:
        return 0
    ans, size = 0, len(height)
    left_max, right_max = [0] * size, [0] * size
    
    left_max[0] = height[0]
    for i in range(1, size):
        left_max[i] = max(height[i], left_max[i-1])
        
    right_max[size-1] = height[size-1]
    for i in range(size-2, -1, -1):
        right_max[i] = max(height[i], right_max[i+1])
        
    for i in range(size):
        ans += min(left_max[i], right_max[i]) - height[i]
        
    return ans

# MORE OPTIMAL SOLUTION O(1) SPACE
def trap2(height):
        
    left, right = 0, len(height) - 1
    ans = 0
    left_max, right_max = 0, 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                ans += (left_max - height[left])
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                ans += (right_max - height[right])
            right -= 1
            
    return ans