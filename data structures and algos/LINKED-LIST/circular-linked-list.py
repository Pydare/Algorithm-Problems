class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def display_list(self):
        if self.last == None:
            print('Empty list')
            return
        p = self.last.link
        while True:
            print(p.info, ' ', end=' ')
            p = p.link
            if p == self.last.link:
                break
        print()

    def insert_beginning(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp

    def insert_emptylist(self, data):
        temp = Node(data)
        self.last = temp
        self.last.link = self.last

    def insert_end(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp
        self.last = temp

    def create_list(self):
        n = int(input('Enter your number of nodes: '))
        if n == 0:
            return
        data = int(input('Enter the elements to be entered: '))
        self.insert_emptylist(data)

        for _ in range(n-1):
            data = int(input('Enter the elements to be entered: '))
            self.insert_end(data)

    def insert_after(self, data, x):
        p = self.last.link
        while True:
            if p.info == x:
                break
            p = p.link
            if p == self.last.link:
                break
        if p == self.last.link and p.info != x:
            print(f'{x} is not present in the list')
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
            if  p == self.last:
                self.last = temp

    def delete_first(self):
        if self.last is None:
            return #no node
        if self.last == self.last.link:
            self.last = None
            return #one node

    def delete_last(self):
        if self.last is None:
            return #no node
        if self.last == self.last.link:
            self.last = None
            return
        p = self.last.link
        while p.link != self.last:
            p = p.link
        p.link = self.last.link
        self.last = p

    def delete_node(self, x):
        if self.last is None:
            return #no node
        if self.last == self.last.link:
            self.last = None
            return
        #delete first node
        if self.last.link.info == x:
            self.last.link = self.last.link.link
            return

        #now to business
        p = self.last.link
        while p.link != self.last.link:
            if p.link.info == x:
                break
            p = p.link
            if p.link == self.last.link:
                print(f'{x} is not found in the list')
            else:
                p.link = p.link.link
                if self.last.info == x:
                    self.last = p

    def concatenate(self, list2):
        if self.last is None:
            self.last = list2.last
            return
        if list2.last is None:
            return

        p = self.last.link
        self.last.link = list2.last.link
        list2.last.link = p
        self.last = list2.last
