class StackEmptyError:
    pass
class StackFullError:
    pass
class Stack:
    def __init__(self, max_size=10):
        self.items = [None] * max_size
        self.count = 0
    def is_full(self):
        return self.count == len(self.items)
    def size(self):
        return self.count
    def is_empty(self):
        return self.count == 0
    def push(self, x):
        if self.is_full():
            print('List is full')
        else:
            self.items[self.count] = x
            self.count += 1
    def pop(self):
        if self.is_empty():
            print('List is empty')
        else:
            popped_item = self.items[self.count-1]
            self.items[self.count-1] = None
            self.count -= 1
            return popped_item
    def peek(self):
        return self.items[self.count-1]
    def display(self):
        print(self.items)

st = Stack()
st = Stack()
while True:
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Size')
    print('5. Display')
    print('6. Quit')

    choice = int(input('Enter the operation you want to carry out: '))
    if choice == 1:
        data = int(input('Enter element to be pushed: '))
        st.push(data)
    elif choice == 2:
        x = st.pop()
        print(f'The popped item is {x}')
    elif choice == 3:
        x = st.peek()
        print(f'The peek element is {x}')
    elif choice == 4:
        x = st.size()
        print(f'The size of the list is {x}')
    elif choice == 5:
        st.display()
    elif choice == 6:
        break
    else:
        print('Wrong option selected')

    