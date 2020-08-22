#2nd implementation -> Faster
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s=[]
        

    def push(self, x: int) -> None:
        if self.s:
            self.s.append((x,min(x,min(self.s[-1][1],x))))
        else:
            self.s.append((x,x))

    def pop(self) -> None:
        if self.s:
            self.s.pop()

    def top(self) -> int:
        if self.s:
            return self.s[-1][0]

    def getMin(self) -> int:
        if self.s:
            return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
"""
#1st implementation
from math import inf
from heapq import heappush,heappop,heapify
class MinStack:

    def __init__(self):
        self.stack=[]
        self.size=0
        self.heap=[]

    def push(self, x: int) -> None:
        self.stack.append(x)
        heappush(self.heap,x)
        self.size+=1

    def pop(self) -> None:
        if self.size:
            self.stack.pop()
            self.heap=self.stack.copy()
            heapify(self.heap)
            self.size-=1
            print(self.stack)

    def top(self) -> int:
        if self.size:
            return self.stack[self.size-1]

    def getMin(self) -> int:
        if self.heap:
            return self.heap[0]
"""


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
