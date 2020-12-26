def droppedRequests(requestTime):
    # Write your code here
    ans = 0
    for i in range(3, len(requestTime)):
        if requestTime[i-3] == requestTime[i]:
            ans += 1
            continue
        if i > 19 and requestTime[i] - requestTime[i-20] < 10:
            ans += 1
            continue
        if i > 59 and requestTime[i] - requestTime[i-60] < 60:
            ans += 1
            continue
    return ans

# 1 1 1 1 2 2 2 3 3 3 4 4 4 5 5 5 6 6 6 7 7 7 7 11 11 11 11