class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self,x):
        #move all elements to s1
        self.s1.append(x)
        

    def deQueue(self):
        #if both stacks are empty
        if len(self.s1)==0 and len(self.s2)==0:
            print('queue is empty')
        #if s2 is empty move elements from s1
        #if len(self.s2) == 0:
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        p = self.s2[-1]
        self.s2.pop()
        return p

q = Queue()
q.enQueue(1)  
q.enQueue(2)  
q.enQueue(3) 

print(q.deQueue())
print(q.deQueue())
print(q.deQueue())