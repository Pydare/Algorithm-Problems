'''
1. start from the second bar, if its not higher than any of the previous
   multiply its height by its index
   if its taller, multiply their distance by the shorter height of the 
   previous
2. if there's a taller one before it, multiply its height by the difference
   between its index and that ones
3. append all multiplications into a list
4. when we have multiple previous bars, 

'''


def maxArea(height):
    l = []
    temp = 0
    area = 0
    beg,end = 0,(len(height)-1)
    first,last = height[beg],height[end]
    while beg < end:
        if first < last:
            temp = first*(end-beg)
        elif first > last:
            temp = last*(end-beg)
        elif first == last:
            temp = first*(end-beg)
        elif end-beg == 0:
            if first < last:
                temp = first*1
            else:
                temp = last*1
        if temp > area:
            l.append(temp)
            area = temp
        temp = 0

        ########
        if first < last:
            beg +=1
        elif last < first:
            end -=1
        
    print(area)

maxArea([1,8,6,2,5,4,8,3,7])