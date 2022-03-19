#Attempt2: in the first attempt, understood the problem wrong: Thought that we
#ahve to delete all occurences of an element
from heapq import heappush,heappop
class FreqStack:

    def __init__(self):
        self.stack_top = 0
        self.number_with_freq = {}
        self.maxheap_freq = []
        self.index_to_val = {}
        
    def push(self, val: int) -> None:
        if val not in self.number_with_freq:
            self.number_with_freq[val] = 0
        self.number_with_freq[val] += 1
        heappush(self.maxheap_freq,(-self.number_with_freq[val],-self.stack_top))
        self.index_to_val[self.stack_top] = val
        self.stack_top += 1

    def pop(self) -> int:
        freq,index = heappop(self.maxheap_freq)
        ans = self.index_to_val[-index]
        self.number_with_freq[ans] -= 1
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
