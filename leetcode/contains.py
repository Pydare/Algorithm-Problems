def  occur(nums,k):
    d = dict()
    for i in range(len(nums)):
        if d.get(nums[i],None) is not None:
            diff = d[nums[i]].append(i)
        else:
            d[nums[i]] = [i]
    for _,v in d.items():
        for i in range(len(v)):
            for j in range(i+1,len(v)):
                diff = abs(v[i]-v[j])
                if diff <= k:
                    return True
    return False

print(occur([1,0,1,1],1))
