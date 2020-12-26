def earliest_delivery_time(buildings, building_opening_time, offload_time):
    # sort both building opening time and offload time
    building_opening_time.sort()
    offload_time.sort()

    res = 0
    for i in range(buildings):
        # each building has 4 docks, assume buildings = buildings *4
        # we can offload 4 items at a time
        idx = buildings * 4 - i * 4 - 1
        # building with earliest time first + max offload time
        res = max(res, building_opening_time[i] + offload_time[idx])

    return res 