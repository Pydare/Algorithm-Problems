from collections import defaultdict

def robot_delivery_system(num_orders, requirements, flask_types, total_marks, markings):
    new_markings = defaultdict(list)
    for x, y in markings:
        new_markings[x].append(y)
    
    max_req = max(requirements)
    min_idx, wasted_units = num_orders - 1, float('inf')

    for i in range(num_orders, -1, -1):
        if max(num_orders[i]) < max_req:
            continue
        temp = get_wasted_units(new_markings[i], requirements)
        if temp <= wasted_units:
            wasted_units = temp
            min_idx = i

    return -1 if min_idx == num_orders-1 else min_idx

def get_wasted_units(marks, requirements):
    res = float('inf')
    max_req = max(requirements)

    for mark in marks:
        if mark < max_req:
            continue
        else:
            temp = 0
            for req in requirements:
                temp += (mark - req)
            res = min(res, temp)

    return res