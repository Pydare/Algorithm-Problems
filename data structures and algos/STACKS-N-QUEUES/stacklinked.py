class EmptyStackError:
    pass 

class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class Stack:
    def __init__(self):
        self.top = None
    def is_empty(self):
        return self.top == None
    def size(self):
        if self.is_empty():
            return 0
        count = 0
        p = self.top
        while p is not None:
            count += 1
            p = p.link
        return count
    def push(self, data):
        temp = Node(data)
        temp.link = self.top
        self.top = temp
    def pop(self):
        if self.is_empty():
            return EmptyStackError('Stack is empty')
        popped = self.top.info
        self.top = self.top.link
        return popped
    def peek(self):
        if self.is_empty():
            return EmptyStackError('Stack is empty')
        return self.top.info
    def display(self):
        if self.is_empty():
            print('Stack is empty')
            return
        print('Stack is: ')
        p = self.top
        while p is not None:
            print(p.info,' ')
            p = p.link

st = Stack()
while True:
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Size')
    print('5. Display')
    print('6. Quit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        x = int(input('Enter element to be pushed: '))
        st.push(x)
    elif choice == 2:
        x = st.pop()
        print(f'Element popped is {x}')
    elif choice == 3:
        print('Element at the top is ',st.peek())
    elif choice == 4:
        print('Stack of size is ', st.size())
    elif choice == 5:
        st.display()
    elif choice == 6:
        break
    else:
        print('Wrong choice')
    print()