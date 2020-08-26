import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo, self.hi = [],[]
        

    def addNum(self, num: int):
        #add to the low heap
        heapq.heappush(self.lo,num)

        #add to the high heap and remove from low heap
        heapq.heappush(self.hi,-self.lo[0])
        heapq.heappop(self.lo)

        #if size if high heap > low heap add top element of high heap to low heap
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo,-self.hi[0])
            heapq.heappop(self.hi)
     

    def findMedian(self):
        return self.lo[0] if len(self.lo) > len(self.hi) else (self.lo[0] + -(self.hi[0]))/2