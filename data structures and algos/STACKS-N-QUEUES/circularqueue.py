class Queue:
    def __init__(self, default_size=10):
        self.items = [None] * default_size 
        self.front = 0
        self.count = 0
    def is_empty(self):
        return self.count == 0
    def size(self):
        return self.count
    def enqueue(self, item):
        if self.count == len(self.items):
            self.resize(2*len(self.items))
        i = (self.front + self.count) % len(self.items)
        self.items[i] = item
        self.count += 1
    def dequeue(self):
        if self.is_empty():
            print('List is empty')
        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return x
    def peak(self):
        if self.is_empty():
            print('The list is empty')
        return self.items[self.front]
    def display(self):
        print(self.items)
    def resize(self, newsize):
        old_list = self.items
        self.items = [None] * newsize
        i = self.front
        for j in range(self.count):
            self.items[j] = old_list[i]
            i = (1+i) % len(old_list)
        self.front = 0

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