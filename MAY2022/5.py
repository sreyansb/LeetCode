#attempt1:
from collections import deque
class MyStack:

    def __init__(self):
        self.append_queue = deque([])
        self.pop_queue = deque([])
        
    def push(self, x: int) -> None:
        self.append_queue.append(x)

    def pop(self) -> int:
        while(len(self.append_queue)>1):
            self.pop_queue.append(self.append_queue.popleft())
        value = self.append_queue.popleft()
        while(self.pop_queue):
            self.append_queue.append(self.pop_queue.popleft())
        return value

    def top(self) -> int:
        while(len(self.append_queue)):
            value = self.append_queue.popleft()
            self.pop_queue.append(value)
        while(self.pop_queue):
            self.append_queue.append(self.pop_queue.popleft())
        return value
    
    def empty(self) -> bool:
        return len(self.append_queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
