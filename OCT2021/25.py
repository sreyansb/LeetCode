#attempt2:
from heapq import heappush,heappop
class MinStack:

    def __init__(self):
        self.li = []
        self.heap=[]
        
    def push(self, val: int) -> None:
        self.li.append(val)
        heappush(self.heap,val)
        
    def pop(self) -> None:
        self.li.pop()
        
    def top(self) -> int:
        return self.li[-1]

    def getMin(self) -> int:
        while(self.heap[0] not in self.li):
            heappop(self.heap)
        return self.heap[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#attempt1:
'''
from heapq import heappush,heappop
class MinStack:

    def __init__(self):
        self.li = []
        
    def push(self, val: int) -> None:
        self.li.append(val)
        
    def pop(self) -> None:
        self.li.pop()
        
    def top(self) -> int:
        return self.li[-1]

    def getMin(self) -> int:
        return min(self.li)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
'''