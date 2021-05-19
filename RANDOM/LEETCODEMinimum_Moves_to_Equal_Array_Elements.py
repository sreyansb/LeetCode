#instead of making incrementing, think of decrementing such that you make 
#all elements equal to minimim
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        return sum(nums)-n*min(nums)
        