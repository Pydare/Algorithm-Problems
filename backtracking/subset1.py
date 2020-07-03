nums = [1,2,3]
def subset(nums):
    output = [[]]

    for num in nums:
        print(output) 
        output += [ curr + [num]  for curr in output ]           #[[],[1]]


def subsets(nums):
    def backtrack(first=0,curr=[]):
        #base case: if the combination is done
        if len(curr) == k:
            output.append(curr[:])

        for i in range(first,n):
            curr.append(nums[i])

            backtrack(i+1,curr)

            curr.pop()

    output = []
    n = len(nums)
    for k in range(n+1):
        backtrack()
    return output 