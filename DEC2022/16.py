#attempt1:
class MyQueue:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        
        newStack = []
        while(self.stack):
            newStack.append(self.stack.pop())
        self.stack.append(x)
        while(newStack):
            self.stack.append(newStack.pop())

    def pop(self) -> int:
        
        return self.stack.pop()

    def peek(self) -> int:
       
        return self.stack[-1]
        
    def empty(self) -> bool:
        
        return self.stack == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
