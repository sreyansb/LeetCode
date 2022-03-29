#attempt2: Used O(n) space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        di={}
        for i in nums:
            if i not in di:
                di[i]=1
            elif di[i]==1:
                return i

#attempt1: WA because I thought only one element is appearing just twice
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(1,n):
            xor ^= i
            xor ^= nums[i-1]
        xor ^= nums[-1]
        return xor
            
'''
