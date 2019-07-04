class Node(object):
    def __init__(self, value):
        self.info = value
        self.link = None

class CircularLinkedList(object):

    def __init__(self):
        self.last = Node

    def display_list(self):
        if self.start == None:
            print('List is empty')
            return

        p = self.last.link

        while True:
            print(p.info, ' ', end='')
            p = p.link
            if p == self.last.link:
                break
        print()

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp

    def insert_in_empty_list(self, data):
        temp = Node(data)
        self.last = temp
        self.last.link = self.last

    def insert_at_end(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.start.link = temp
        self.last = temp

    def create_list(self):
        n = int(input('Enter the number of nodes: '))
        if n == 0:
            return
        data = int(input('Enter the element to be inserted: '))
        self.insert_in_empty_list(data)

        for i in range(n-1):
            data = int(input('Enter the element to be inserted: '))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        p = self.last.link

        while True:
            if p.info == x:
                break
            p = p.link
            if p == self.last.link:
                break
        
        if p == self.last.link and p.info != x:
            print(x, ' not present in the list')
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
            if p == self.last:
                self.last = temp
        
