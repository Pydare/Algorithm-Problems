class MinHeap:
    def __init__(self,maxsize):
        self.a = [None]*maxsize
        self.n = 0
        self.a[0] = 9999999
    def insert(self,value):
        self.n += 1
        self.a[self.n] = value
        self.restore_up(self.n)
    def restore_up(self,i):
        k = self.a[i]
        iparent = i//2
        while self.a[iparent] > k and iparent >= 1: 
            self.a[i] = self.a[iparent]
            i = iparent
            iparent = i // 2
        self.a[i] = k
    def delete(self):
        if self.n == 0:
            print('Heap is empty')
        minValue = self.a[1]
        self.a[1] = self.a[self.n]
        self.n -= 1
        self.restore_down(1)
        return minValue
    def restore_down(self,i):
        k = self.a[i]
        l = 2*i
        r = l+1
        while r <= self.n:
            if k <= self.a[l] and k <= self.a[r]:
                self.a[i] = k
                return
            else:
                if self.a[l] < self.a[r]:
                    self.a[i] = self.a[l]
                    i = l
                else:
                    self.a[i] = self.a[r]
                    i = r
            l = 2*i
            r = l+1
            
        #if number of nodes is even
        if l == self.n and k > self.a[l]:
            self.a[i] = self.a[l]
            i = l
        self.a[i] = k
            



#h = Heap(n)
def mergeKsorted(lists):
    l = []
    tracker_a,tracker_b,tracker_c = 1,1,1
    h = MinHeap(len(lists)+1)
    h.insert(lists[0][0])
    h.insert(lists[1][0])
    h.insert(lists[2][0])

    m = h.delete()
    l.append(m)
    
    while (tracker_a <= len(lists[0])-1) and (tracker_b <= len(lists[0])-1) and (tracker_c <= len(lists[0])-1):
        if m in lists[0]:
            h.insert(lists[0][tracker_a])
            m = h.delete()
            l.append(m)
            tracker_a += 1
        elif m in lists[1]:
            h.insert(lists[1][tracker_b])
            m = h.delete()
            l.append(m)
            tracker_b += 1
        elif m in lists[2]:
            h.insert(lists[2][tracker_c])
            m = h.delete()
            l.append(m)
            tracker_c += 1
    
    return l

print(mergeKsorted([[1,3,5,7],[2,4,6,8],[0,9,10,11]]))
