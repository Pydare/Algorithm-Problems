#backtracking solution
def can_jump(nums):
    return can_jump_from_position(0,nums)

def can_jump_from_position(position,nums):
    #base case
    if position == len(nums)-1:
        return True
    
    furthest_jump = min(position+nums[position], len(nums)-1)
    for next_position in range(position+1,furthest_jump):
        if can_jump_from_position(next_position,nums):
            return True
        
    return False

"""
[2,3,1,1,4]
"""
##backtracking + memoization
def can_jump_memo(nums):
    GOOD, BAD, UNKNOWN = 0, 1, -1

    def can_jump_memo_helper(position,nums):
        if memo[position] != UNKNOWN:
            return True if GOOD else False
        
        furthest_jump = min(position+nums[position], len(nums)-1)
        for next_position in range(position+1, furthest_jump):
            if can_jump_memo_helper(next_position,nums):
                memo[position] = GOOD
                return True
                
        memo[position] = BAD
        return False

    memo = [UNKNOWN]*len(nums)
    memo[len(nums)-1] = GOOD
    return can_jump_memo_helper(0,nums)

##DP bottom up approach
def can_jump_dp(nums):
    GOOD, BAD, UNKNOWN = 0, 1, -1
    memo = [UNKNOWN] * len(nums)
    memo[len(nums)-1] = GOOD

    for i in range(len(nums)-2,-1,-1):
        furthest_jump = min(i+nums[i], len(nums)-1)
        for j in range(i+1,furthest_jump):
            if memo[j] == GOOD:
                memo[i] = GOOD
                break

    return memo[0] == GOOD  

res = can_jump_dp([2,3,1,1,4])
print(res)