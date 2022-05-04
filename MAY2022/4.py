#attempt1:
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        di = {}
        ans = 0
        for i in nums:
            if k-i in di:
                ans += 1
                di[k-i] -= 1
                if di[k-i] == 0:
                    del di[k-i]
            else:
                if i not in di:
                    di[i] = 0
                di[i] += 1
        return ans
                
                
        
