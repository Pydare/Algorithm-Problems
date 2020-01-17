def runningMedian(l):
    tracker,median,j = [],[],0
    for i in range(len(l)):
        while j < i+1:
            tracker.append(l[j])
            tracker.sort()
            j+=1
        if len(tracker)%2 == 0:
            q = len(tracker)//2
            p = q-1
            middle = (tracker[q]+tracker[p])/2
            median.append(middle)
        if len(tracker)%2 != 0:
            q = len(tracker)//2
            median.append(tracker[q])
    print(median)

runningMedian([2,1,5,7,2,0,5])