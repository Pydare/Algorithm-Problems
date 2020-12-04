def winner(num, lower_end, upper_end):
    if (upper_end - lower_end) + 1 < num:
        return -1

    res = [0] * num
    mid_r = num//2
    mid_l = mid_r - 1

    # filling up the first half
    temp = upper_end
    while mid_l >= 0:
        res[mid_l] = temp
        mid_l -= 1
        temp -= 1

    # filling up the second half
    temp = upper_end - 1
    while mid_r < num:
        res[mid_r] = temp
        mid_r += 1
        temp -= 1

    return res

ans = winner(3, 1, 3)
#print(ans)

###############LEETCODE SOLUTION#########################
def solution(num, lower_end, upper_end):
    delta = upper_end - lower_end 

    # we cannot form a sequence, there are not enough numbers
    if num > 2 * (delta + 1):
        return -1

    # if we can form a sequence, assume that the element to the left of upper is the starting one
    starting_number = upper_end - 1

    # move to the left until we can form a sequence
    while (((upper_end-starting_number) + 1) + delta) < num:
        starting_number -= 1

    # construct the array
    res = [0] * num
    i = 0

    # this will fill elements in strictly increasing order
    while starting_number < upper_end:
        res[i] = starting_number
        i += 1
        starting_number += 1

    res[i] = starting_number 

    while i < num:
        res[i] = starting_number
        i += 1
        starting_number -= 1

    return res

ans = solution(5, 1, 3)
print(ans)