from queue import PriorityQueue

q = PriorityQueue()
random = [57,32,2,90,2,1,12,44,41,76,18,9,32]

q.put(1,'a')
q.put(12,'b')
q.put(1,'c')
q.put(3,'d')

while not q.empty():
    temp = q.get()
    print(temp)