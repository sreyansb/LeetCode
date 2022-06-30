#attempt3: IT is median you dumb idiot
from math import ceil,floor
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        median = 0
        if n%2:
            median = nums[n//2]
        else:
            median = (nums[(n//2)]+nums[(n-1)//2])//2
        return sum([abs(i-median) for i in nums])

#attempt2:
'''
from math import ceil,floor
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        meanhigher = ceil(sum(nums)/len(nums))
        meanlower = sum(nums)//len(nums)
        return min(sum([abs(meanhigher-i) for i in nums]),sum([abs(i-meanlower) for i in nums]))
        
'''

#attempt1:
'''
from math import ceil
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        mean = ceil(sum(nums)/len(nums))
        return sum([abs(mean-i) for i in nums])
        
'''
