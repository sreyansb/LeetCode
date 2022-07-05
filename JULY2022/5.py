#attempt2:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not(nums):
            return 0
        nums = sorted(set(nums))
        maxcount = 1
        prev = float('inf')
        currentcount = 0
        for i in nums:
            if i != prev+1:
                currentcount = 0
            prev = i
            currentcount += 1
            maxcount = max(maxcount,currentcount)
        return maxcount

#attempt1: WA because didn't do empty check on nums
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        maxcount = 1
        prev = float('inf')
        currentcount = 0
        for i in nums:
            if i != prev+1:
                currentcount = 0
            prev = i
            currentcount += 1
            maxcount = max(maxcount,currentcount)
        return maxcount
'''
            
