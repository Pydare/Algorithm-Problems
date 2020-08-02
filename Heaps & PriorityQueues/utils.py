from queue import PriorityQueue

q = PriorityQueue()
random = [57,32,2,90,2,1,12,44,41,76,18,9,32]

q.put('a')
q.put('b')
q.put('c')
q.put('d')

while not q.empty():
    temp = q.get()
    print(temp)