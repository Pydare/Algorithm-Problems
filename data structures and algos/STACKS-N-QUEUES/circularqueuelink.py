class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class Queue:
    def __init__(self):
        self.rear = None
    def is_empty(self):
        return self.rear == None
    def size(self):
        if self.is_empty():
            return 0
        n = 0
        p = self.rear.link
        while True:
            n += 1
            p = p.link
            if p == self.rear.link:
                break
        return n
    def enqueue(self, data):
        temp = Node(data)
        if self.is_empty():
            self.rear = temp
            self.rear.link = self.rear
        else:
            temp.link = self.rear.link
            self.rear.link = temp
            self.rear = temp
    def dequeue(self):
        if self.is_empty():
            print('The list is empty unfortunately')
        if self.rear.link == self.rear: #list has only one node
            temp = self.rear
            self.rear = None
        else:
            temp = self.rear.link
            self.rear.link = self.rear.link.link
        return temp.info

    def peak(self):
        if self.is_empty():
            print('The list is empty, do something about it before I snap')
            return
        print('The peak of the list is ', self.rear.link.info)
    
    def display(self):
        if self.is_empty():
            print('The list is empty')
            return
        p = self.rear.link
        while True:
            print(p.info, ' ', end = '')
            p = p.link
            if p == self.rear.link:
                break
        print()

qu = Queue()

while True:
    print('1. Enqueue')
    print('2. Dequeue')
    print('3. Peek')
    print('4. Size')
    print('5. Display')
    print('6. Quit')

    choice = int(input('Enter the element: '))

    if choice == 1:
        x = int(input('Enter the element: '))
        qu.enqueue(x)
    elif choice == 2:
        x = qu.dequeue()
        print(f'The element deleted from the queue is {x}')
    elif choice == 3:
        print('Element at the front of the queue is ', qu.peak())
    elif choice == 4:
        x = qu.size()
        print(f'The size of the queue is {x}')
    elif choice == 5:
        qu.display()
    elif choice == 6:
        break
    else:
        print('You entered the wrong choice, try again')
