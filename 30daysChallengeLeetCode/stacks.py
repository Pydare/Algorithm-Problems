class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] 
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        i = self.stack.index(self.stack[-1])
        while i >= 1  and self.stack[i] > self.stack[i-1]:
            self.stack[i], self.stack[i-1] = self.stack[i-1], self.stack[i]  
            i -= 1
        

    def pop(self) -> None:
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[-1]
    
    def getStack(self):
        return self.stack

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)

obj.getMin()   
r = obj.getStack() 
print(r)
obj.pop()
obj.top()  
   
#obj.getMin()