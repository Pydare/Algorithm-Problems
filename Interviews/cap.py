def change(num):
    for mul_7 in range(5):
        if (num - (7*mul_7)) % 5 == 0:
            mul_5 = (num - (7*mul_7)) // 5
    return ([5] * mul_5) + ([7] * mul_7)


print(change(89))