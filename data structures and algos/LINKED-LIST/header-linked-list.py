class Node:
    def __init__(self, value):
        self.info = value
        self.link = None
    

class HeaderLinkedList:
    def __init__(self):
        self.head = Node(0)

    def display_list(self):
        if self.head.link == None:
            print('List is empty gah damn')
            return
        p = self.head.link
        print('List is: ')
        while p is not None:
            print(p.info, ' ', end='')
            p = p.link
        print()

    def create_list(self):
        n = int(input(("Enter the number of nodes: ")))
        for i in range(n):
            data = int(input("Enter the elements to be inserted: "))
            self.insert_end