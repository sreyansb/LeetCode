#attempt1: Couldn't understand the radix sort part
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:
            return 0
        nums=set(nums)
        
            