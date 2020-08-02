class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def add_to_beginning(self,val):
        temp = Node(val)
        if not self.head:
            self.head = temp
            return
        temp.prev = None #not compulsory
        temp.next = self.head
        self.head.prev = temp
        self.head = temp 

    def add_at_end(self,val):
        temp = Node(val)
        if not self.head:
            self.head = temp
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p

    def add_before(self,x,val):
        temp = Node(val)
        if not self.head:
            return
        if not self.head.next and self.head.val == x:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

        p = self.head
        while p is not None:
            if p.val == x:
                break 
            p = p.next
        if p is None:
            print("x not found")
            return
        else:
            temp.next = p
            temp.prev = p.prev
            p.prev.next = temp
            p.prev = temp

    def add_after(self,x,val):
        temp = Node(val)
        if not self.head:
            return

        p = self.head
        while p is not None:
            if p.val == x:
                break
            p = p.next
        if p is None:
            print("x not in the list")
            return
        else:
            temp.prev = p
            temp.next = p.next
            if p.next is not None:
                p.next.prev = temp # should not be done when p refers to last nodes
            p.next = temp 

    def reverse(self):
        if not self.head or not self.head.next:
            return
        p1 = self.head
        p2 = p1.next
        p1.next = None
        p1.prev = p2

        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev
        self.head = p1
        
        
