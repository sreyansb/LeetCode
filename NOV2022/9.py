#attempt4: TOOK HINT that stack is needed

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = -1
    
    def next(self, price: int) -> int:
        self.index += 1
        while(self.stack and self.stack[-1][0] <= price):
            self.stack.pop()
        if self.stack:
            startIndex = self.stack[-1][1]
        else:
            startIndex = -1
        self.stack.append((price,self.index))
        print(self.stack,startIndex)
        return self.index - startIndex
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

#attempt3: TLE 87/99
'''

class StockSpanner:

    def __init__(self):
        self.list = []
        self.len = 0
    
    def next(self, price: int) -> int:
        current_index = self.len - 1
        while(current_index > -1 and self.list[current_index] <= price):
            current_index -= 1
        ans = self.len - current_index
        self.list.append(price)
        self.len += 1
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
'''

#attempt2:WA 51/99
'''
class StockSpanner:

    def __init__(self):
        self.list = []
        self.len = 0
    
    def next(self, price: int) -> int:
        current_index = self.len - 1
        while(current_index > -1 and self.list[current_index] < price):
            current_index -= 1
        ans = self.len - current_index
        self.list.append(price)
        self.len += 1
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
'''


#attempt1: WA - didn't understand the question properly
'''
from sortedcontainers import SortedList
class StockSpanner:
    def __init__(self):
        self.list = SortedList([])       

    def next(self, price: int) -> int:
        self.list.add(price)
        pos = self.list.bisect_right(price)
        return pos
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
'''
