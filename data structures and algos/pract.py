class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class SingleLinkedList:
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            return 'The list is empty'
        else:
            p = self.start
            print('Elememts in the list are: ')
            while p is not None:
                print(p.info, ' ', end=' ')
                p = p.link
            print()

    def count_nodes(self):
        if self.start is None:
            return 'The number of nodes is 0'
        else:
            count = 0
            p = self.start
            while p is not None:
                count += 1
                p = p.link
            return f'The number of nodes is {count}'

    def search(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(f'{x} is at position, {position}')
                return True
            position += 1
            p = p.link
        else:
            print(f'{x} is not found in the list')
            return False

    def insert_at_beginning(self):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self):
        temp = Node(data)
        if self.start is None:
            self.start = temp
        p = self.start
        while p is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter the number of nodes for your list: "))
        if n == 0:
            return
        for i in range(n):
            data = int(input(f'Enter node to be inserted at position {i}: '))
            self.insert_at_end(data)

    def reverse_list(self):
        prev = None
        p = self.start
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    def bubble_sortdata(self):
        end = None:
        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p

    def bubble_sortlinks(data):
        end = None
        while end != self.start.link:
            r = p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.link = q.link
                    q.link = p
                    if p != self.start:
                        r.link = q
                    else:
                        self.start = q
                    p,q = q,p
                r = p
                p = p.link
            end = p

    def find-cycle(self):
        if self.start is None or self.start.link is None:
            return None
        slowR = self.start
        fastR = self.start
        while fastR is not None or fastR.link is not None:
            slowR = slowR.link
            fastR = fastR.link.link
            if slowR == fastR:
                return slowR
        return None

            