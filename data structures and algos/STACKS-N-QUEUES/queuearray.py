class Queue:
    def __init__(self):
        self.items = []
        self.front = 0
    def isempty(self):
        return self.front == len(self.items)
    def size(self):
        return len(self.items) - self.front
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.isempty():
            print('Queue is empty')
        x = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        return x
    def peak(self):
        if self.isempty():
            print('The list is empty dawg')
        return self.items[self.front]
    def display(self):
        print(self.items)

qu = Queue()
while True:
    print('1. Enqueue')
    print('2. Dequeue')
    print('3. Size')
    print('4. Peek')
    print('5. Display')
    print('6. Quit')

    option = int(input('Select the number option you want: '))

    if option == 1:
        x = int(input('Enter number to be enqueued: '))
        qu.enqueue(x)
    elif option == 2:
        x = qu.dequeue()
        print(f'The dequeued element is {x}')
    elif option == 3:
        x = qu.size()
        print(f'Size of queue is {x}')
    elif option == 4:
        x = qu.peak()
        print(f'The peak of the queue is {x}')
    elif option == 5:
        qu.display()
    elif option == 6:
        break
    else:
        print('Invalid option')
