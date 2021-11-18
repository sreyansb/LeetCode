#attempt1:
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        finarr = [0 for i in range(n+1)]
        for i in nums:
            finarr[i] = 1
        return [i for i in range(1,n+1) if finarr[i]==0]
