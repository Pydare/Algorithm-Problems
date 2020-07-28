"""
given n planets ---> [3,5,2,1,4,7]
given planet position ---> 0
return k closest planets

assumptions
1. can i fit all the n planets into memory;
2. do i have duplicates in my array
3. could my k<=0 or k>=n
4. all positive or negative
5. are they sorted

x = (1,2,3)  planets = [3,5,2,1,4,7]  k=2

"""
import heapq

class MaxHeap:
    def __init__(self,data=[]):
        self.data = data

    def top(self):
        return self.data[0]

    def push(self, val):
        heapq.heappush(self.data, val)

    def pop(self):
        return heapq.heappop(self.data)

    def heapify(self):
        return heapq.heapify(self.data)

# def euclidean(p,x):
#     return []

def closest_planets(planets,k,x):
    #planets = euclidean(planets,x)
    heap = MaxHeap(planets[:k])              #[2,1]
    heap.heapify()

    for planet in planets[k:]:
        if planet < heap.data[0]:
            heap.push(planet)
            heap.heapify()
            print(heap.data.reverse())
            heap.pop()
            
    return heap.data

res = closest_planets([3,5,2,1,4,7],2,0)
print(res)

