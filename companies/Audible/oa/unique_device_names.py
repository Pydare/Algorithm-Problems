def unique(nums, device_names):
    res = []
    hash_table = {}

    for i in range(nums):
        if device_names[i] in hash_table:
            hash_table[device_names[i]] += 1
            res.append(device_names[i] + str(hash_table[device_names[i]]))
        else:
            hash_table[device_names[i]] = 0
            res.append(device_names[i])

    return res

ans = unique(8, ["switch", "tv", "switch", "tv","switch", "tv", "tv", "tv"])
print(ans)