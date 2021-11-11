#attempt1:
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        arr = [0]
        for i in nums:
            arr.append(arr[-1]+i)
        return -min(arr)+1
        
