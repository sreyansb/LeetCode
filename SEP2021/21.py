#attempt1:
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxoverall=0
        curlen=0
        for i in nums:
            if i:
                curlen+=1
            else:
                maxoverall=max(maxoverall,curlen)
                curlen=0
        return max(maxoverall,curlen)