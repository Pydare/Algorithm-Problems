class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def create_linkedlist(self):
        n = int(input("Enter the number of nodes you want: "))
        for _ in range(n):
            value = int(input("Enter node value: "))
            self.add_to_end(value)

    def add_to_beginning(self,val):
        temp = Node(val)
        if not self.head:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def add_to_end(self,val):
        temp = Node(val)
        if not self.head:
            self.head = temp
            return 
        
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = temp 

    def add_before_node(self,x,val):
        temp = Node(val)
        if not self.head:
            return
        if not self.head.next:
            if self.head.val == x:
                temp.next = self.head
                self.head = temp
                return 
            else:
                print("x not in linkedlist")
                return

        p = self.head
        while p is not None:
            if p.next.val == x:
                break
            p = p.next
        
        if p is None:
            print('x not found')
            return
        temp.next = p.next
        p.next = temp

    def add_after_node(self,x,val):
        temp = Node(val)
        if not self.head:
            return 
        if not self.head.next:
            if self.head.val == x:
                self.head.next = temp
                return
            else:
                print('x is not in linkedlist')
                return 
        p = self.head
        while p is None:
            if p.val == x:
                break
            p = p.next

        if p is None:
            print('p not found')
            return 
        if p.next is None:
            p.next = temp
        else:
            temp.next = p.next
            p.next = temp 

    def reverse(self):
        if not self.head or not self.head.next:
            return
        prev = None
        p = self.head
        while p is not None:
            nxt = p.next
            p.next = prev
            prev = p
            p = nxt
        self.head = prev

    def reverse_recur(self):

        def helper(p,prev):
            #base case
            if not p:
                self.head = prev
                return 
            nxt = p.next
            p.next = prev
            helper(nxt,p)   
        prev = None
        p = self.head
        helper(p,prev)  

    def delete(self,x):
        if not self.head:
            return
        if not self.head.next:
            if self.head.val == x:
                self.head = None
                return
            else:
                print('x not in linkedlist')
                return  

        #find reference to x
        p = self.head
        while p is not None:
            if p.next.val == x:
                break
            p = p.next
        #if p is none
        if not p:
            print("x not found")
            return
        #if p is the last Node
        if p.next.next is None:
            p.next = None
        else:
            p.next = p.next.next 

    def find_cycle(self):
        if not self.head or self.head.next:
            return
        t =  h = self.head  

        while t is not None and h is not None:
            t = t.next
            h = h.next.next
            if t == h:
                return t
        return False

    def remove_cycle(self):
        c = self.find_cycle()
        if c is None:
            return
        p = q = c
        len_cycle = 0

        while True:
            len_cycle += 1
            q = q.next
            if p == q:
                break
        print("length id cycle is ", len_cycle)

        len_rem_list = 0
        p = self.head
        while p != q:
            len_rem_list += 1
            p = p.next
            q = q.next

        len_list = len_cycle + len_rem_list

        p = self.head
        for _ in range(len_list):
            p = p.next
        p.next = None 
