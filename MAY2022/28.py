#attempt1:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        curindex = 0
        for num in nums:
            xor ^= curindex
            xor ^= num
            curindex += 1
        xor ^= curindex
        return xor
        
