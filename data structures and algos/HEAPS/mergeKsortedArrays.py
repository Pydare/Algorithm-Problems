def mergeEmAll(a,b,c):
    n = len(a)
    k = 3
    output,minheap = [],[]
    minheap.append(a.pop(0))
    minheap.append(b.pop(0))
    minheap.append(c.pop(0))
    
    heapify(minheap)

    while len(minheap) != 0:
        first = minheap.pop(0)
        output.append(first)
        if first in a:
            minheap.append(a.pop(0))
        elif first in b:
            minheap.append(b.pop(0))
        elif first in c:
            minheap.append(c.pop(0))
        if len(minheap) > 2:
            heapify(minheap)
    
    return output

def heapify(x):
    m = len(x)-1
    val = x[m]
    iparent = (m)//2
    while x[iparent] < val and iparent >=1:
        x[m] = x[iparent]
        m = iparent
        iparent = m//2
    x[m] = val
    return x

print(heapify([1,2,0]))
#print(mergeEmAll([1,3,5,7],[2,4,6,8],[0,9,10,11]))