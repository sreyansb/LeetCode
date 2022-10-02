#attempt3:
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 1000000007
        if not(1<=target<=n*k):
            return 0
        if target == n*k:
            return 1
        @lru_cache(None)
        def findAll(n,target):
            if target == 0:
                return n == 0
            ans = 0
            for numOnFace in range(1,min(k+1,target+1)):
                ans += findAll(n-1,target - numOnFace)
            return ans%mod
        return findAll(n,target)
                
                
        
