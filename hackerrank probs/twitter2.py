def balancedSum(sales):
    total_sum = sum(sales)
    left_sum = 0
    for i, val in enumerate(sales):
        total_sum -= val
        if left_sum == total_sum:
            return i
        left_sum += val

    return -1

print(balancedSum([1,2,3,4,6]))