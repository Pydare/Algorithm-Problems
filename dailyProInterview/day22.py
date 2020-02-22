def merge(intervals):
    for i in range(len(intervals)-2):
        if intervals[i+1][0] <= intervals[i][1]:
            intervals[i][1] = intervals[i+1][1]
            intervals.pop(intervals.index(intervals[i+1]))
    return intervals


print(merge([[1,3],[2,6],[8,10],[15,18]]))
