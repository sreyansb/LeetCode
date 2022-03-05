#attempt1: TOOK HINT
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = max(nums)+1
        arr = [0 for i in range(n)]
        for i in nums:
            arr[i] += 1
        @lru_cache(None)
        def maxie(index):
            if index>=n:
                return 0
            if arr[index] == 0:
                return maxie(index+1)
            return max(index*arr[index]+maxie(index+2),maxie(index+1))
        return maxie(1)
        
            
        
        
