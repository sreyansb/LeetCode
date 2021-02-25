#attempt1:
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        k=sorted(nums)
        if nums==k:
            return 0
        start=-1
        end=-1
        for i in range(len(k)):
            if nums[i]==k[i]:
                continue
            if start==-1:
                start=i
            else:
                end=i
        return end-start+1
            
        
