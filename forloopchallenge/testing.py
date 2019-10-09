def trap(height):
    l = [] 
    i = 0 
    while i < len(height):
        j = i+1
        while j < len(height): 
            if height[j] >= height[i]: 
                diff = height[i]*(j-i)
                l.append(diff) 
                break 
            j += 1   
        i = j       
    print((l))


trap([0,1,0,2,1,0,1,3,2,1,2,1])

        