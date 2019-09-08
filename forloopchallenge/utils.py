class Node:
    def __init__(self, value):
        self.info = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp
    def print(self):
        p = self.head
        while p is not None:
            print(p.info,  ' ', end = '')
            p = p.next
    def removeDuplicates(self):
        d = {}
        p = self.head
        while p is not None:
            if d.get(p, None) is not None:
                d[p] += 1
            else:
                d[p] = 1
            p = p.next
        for key, _ in d.items():
            temp = Node(key)
            temp.next = self.head
            self.head = temp
        return self.head
    def swapNodes(self,x,y):
        p = self.head
        first = Node(x)
        second = Node(y)
        while p.next.info is not x:
            p.next = second
            second.next = p.next.next
            p.next.next = first
            first.next = second.next
            p = p.next
    def swapPairWise(self):
        temp = self.head 
        if temp is None: 
            return 
        while(temp is not None and temp.next is not None): 
            temp.info, temp.next.info = temp.next.info, temp.info   
            temp = temp.next.next
    def moveToFront(self):
        p = self.head
        while p.next is not None:
            temp = p
            p = p.next
        temp.next = None
        p.next = self.head
        self.head = p
    def intersection(self,l1,l2):
        l3 = LinkedList()
        
        

            


li = LinkedList()
li.insert(1)
li.insert(2)
li.insert(3)
li.insert(4)
li.insert(5)
li.insert(6)
#li.insert(7)
li.moveToFront()
li.print()

            
