def three_sum(nums):
    nums.sort()

    def two_sum(arr,target):
        seen, ret = {}, []

        for num in arr:
            if target-num in seen:
                if [num,target-num] not in ret:
                    ret.append([num,target-num])
            seen[num] = True
        return ret