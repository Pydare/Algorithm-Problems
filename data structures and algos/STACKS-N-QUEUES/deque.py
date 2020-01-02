class Deque:
    def __init__(self, default_size=10):
        self.items = [None] * default_size
        self.front = 0
        self.count = 0
    def is_empty(self):
        return self.count == 0
    def size(self):
        return self.count
    def insert_front(self, item):
        if self.count == len(self.items):
            self.resize(2 * len(self.items))
        self.front = (self.front - 1) % len(self.items)
        self.items[self.front] = item
        self.count += 1
    def insert_rear(self, item):
        if self.count == len(self.items):
            self.resize(2 * len(self.items))
        self.front = (self.front + self.count) % len(self.items)
        self.items[self.front] = item
        self.count += 1
    def delete_front(self):
        if self.is_empty():
            print('The list is empty, fill up')
        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return x
    def delete_rear(self):
        if self.is_empty():
            print('The list is empty')
        x = self.items[self.front + self.count]
        self.items[self.front + self.count - 1] = None
        self.count -= 1
        return x
    def first(self):
        if self.is_empty():
            print('The list is empty')
        return self.items[self.first]
    def last(self):
        if self.is_empty():
            print('The list is empty')
        return self.items[self.front + self.count -1]
    def display(self):
        print(self.items)
    def resize(self, new_size):
        old_list = self.items
        self.items = [None] * new_size
        i = self.front
        for j in range(self.count):
            self.items[j] = old_list[i]
            i = (i+1) % len(old_list)
        self.front = 0

qu = Deque()

while True:
    print('1. Insert at the front end')
    print('2. Insert at the rear end')
    print('3. Delete from the front end')
    print('4. Delete from the rear end')
    print('5. Display first element')
    print('6. Display last element')
    print('7. Display')
    print('8. Size')
    print('9. Quit')

    option = int(input('Enter your option: '))

    if option == 1:
        data = int(input('Enter value to be inserted at front end: '))
        qu.insert_front(data)
    elif option == 2:
        data = int(input('Enter value to be inserted at rear end: '))
        qu.insert_rear(data)
    elif option == 3:
        x = qu.delete_front()
        print(f'Your deleted value is {x}')
    elif option == 4:
        x = qu.delete_rear()
        print(f'Your deleted value is {x}')
    elif option == 5:
        qu.first()
    elif option == 6:
        qu.last()
    elif option == 7:
        qu.display()
    elif option == 9:
        break
    else:
        print('You have selected a wrong choice, pick again')
