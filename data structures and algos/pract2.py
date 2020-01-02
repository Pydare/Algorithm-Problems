class Node:
    def _init__(self, value):
        self.info = value
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print('List is empty')
            return
        else:
            print('List is: ')
            p = self.start
            while p is not None:
                print(p.info, ' ', end=' ')
            print()

    def insert_beginning(self, data):
        temp = Node(data)
        temp.next = self.start
        self.start.prev = temp
        self.start = temp 

    def insert_end(self, data):
        temp = Node(data)
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p

    def insert_after(self, data, x):
        temp = Node(data)
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.next
        if p is None:
            print(f'There is no {x} in the list')
        else:
            temp.prev = p
            temp.next = p.next
            if p.next is not None:
                p.next.prev = temp
            p.next = temp

    def insert_before(self):
        if self.start is None:
            print('List is empty')
            return
        if self.start.info == x:
            temp = Node(data)
            temp.next = self.start
            self.start.prev = temp
            self.start = temp
            return
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.next

        if p is None:
            print('{x} is not in the list')
        else:
            temp = Node(data)
            temp.prev = p.prev
            temp.next = p
            p.prev.next = temp
            p.prev = temp

    def delete_first(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return
        self.start = self.start.next
        self.start.prev = None

    def delete_last(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return
        p = self.start
        while p.next != None:
            p = p.next
        p.prev.next = None

    def delete_node(self, x):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
        else:
            print(f'{x} is not found')
        return

        #deletion of first node
        if self.start.info == x:
            self.start = self.start.next
            self.start.prev = None
            return
        p = self.start.next
        while p.next is not None:
            if p.info == x:
                break
            p = p.next

        #node to be deleted is in between
        if p.next is not None:
            p.prev.next = p.next
            p.next.prev = p.prev
        else: #deleting the last node
            if p.info == x:
                p.prev.next = None
            else:
                print(f'{x} is not found')

    def reverse(self):
        if self.start is None:
            return
        p1 = self.start
        p2 = p1.next
        p1.next = None
        p1.prev = p2
        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev
        self.start = p1
