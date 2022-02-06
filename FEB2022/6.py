#attempt1: Partitioning an array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        filledindex = 0
        n = len(nums)
        i = 0
        while(i<n):
            ele = nums[i]
            count = 0
            while(i<n and nums[i]==ele):
                if count != 2:
                    nums[filledindex] = ele
                    filledindex += 1
                    count += 1
                i += 1
        return filledindex
                    
        
