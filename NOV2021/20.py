#attempt1:
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor ^= i
        return xor
            
