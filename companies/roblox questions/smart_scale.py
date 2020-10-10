from collections import defaultdict
def delete_products(ids,m):
    hash_map = defaultdict(int)

    for i in ids:
        hash_map[i] += 1

    while m > 0:
        min_key = min(hash_map, key=hash_map.get)
        hash_map[min_key] -= 1
        m -= 1
        if hash_map[min_key] == 0:
            del hash_map[min_key]

    return len(hash_map)

res = delete_products([1,2,3,1,2,2],3)
print(res)

