#attempt2:
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sumtotal = sum(nums)
        if sumtotal%2:
            return False
        @lru_cache(None)
        def partition(index,sum1):
            
            if index==n:
                if sum1==sumtotal-sum1:
                    return True
                return False
            return partition(index+1,sum1+nums[index]) or partition(index+1,sum1)
        
        return partition(0,0)
            
        

#attempt1: TLE didn't check for totalsum to be even
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sumtotal = sum(nums)
        @lru_cache(None)
        def partition(index,sum1):
            
            if index==n:
                if sum1==sumtotal-sum1:
                    return True
                return False
            
            return partition(index+1,sum1+nums[index]) or partition(index+1,sum1)
        return partition(0,0)
            
        
'''
