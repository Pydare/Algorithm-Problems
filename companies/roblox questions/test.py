def common(inputs):
    total = 0
    res = []
    for inputt in inputs:
        for i in range(1,len(inputt)):
            count = 0
            for j in range(i, len(inputt)):
                if inputt[j-i] != inputt[j]:
                    break
                count += 1
            total += count
        res.append(total)
    return total

res = common(['ababaa','ababaa'])
print(res)