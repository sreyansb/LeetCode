#attempt1:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = 0
        for i in nums:
            number ^= i
        return number
        
