#attempt1: random module in Python
#or you can use knuth shuffle wherein you shuffle and get randome places from 0 to i 
from random import shuffle
class Solution:

    def __init__(self, nums: List[int]):
        self.original=nums.copy()
        self.current=nums.copy()
        

    def reset(self) -> List[int]:
        self.current=self.original.copy()
        return self.current
        
    def shuffle(self) -> List[int]:
        shuffle(self.current)
        return self.current


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()