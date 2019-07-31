class Node:
    def __init__(self, value):
        self.info = value
        self.link = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size_queue = 0
    def is_empty(self):
        return self.front == None
    def size(self):
        return self.size_queue
    def enqueue(self, data):
        temp = Node(data)
        if self.front == None:
            self.front = temp
        else:
            self.rear.link = temp
        self.rear = temp
        self.size_queue += 1
    def dequeue(self):
        if self.is_empty():
            print('The list is empty')
        x = self.front.info
        self.front = self.front.ink
        self.size_queue -= 1
        return x
    def peak(self):
        if self.is_empty():
            print('The list is empty') 
        return self.front.info
    def display(self):
        if self.is_empty():
            print('The list is empty')
            return
        print('The queue is: ')
        p = self.front
        while p is not None:
            print(p.info, ' ', end='')
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
        