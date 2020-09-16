class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n=len(ring)
        m=len(key)
        def dp(index,indexring,cost):
            print(index,indexring,cost)
            if index==m:
                return cost
            if indexring>=n:
                    return float('inf')
            if key[index]==ring[indexring]:
                if indexring==0:
                    return min(dp(index+1,1,cost+1),dp(index+1,n-1,cost+1))
                elif indexring==n-1:
                    return min(dp(index+1,0,cost+1),dp(index+1,indexring-1,cost+1))
                else:
                    return min(dp(index+1,indexring+1,cost+1),dp(index+1,indexring-1,cost+1))
            else:
                if indexring==0:
                    return min(dp(index,1,cost+1),dp(index,n-1,cost+1))
                elif indexring==n-1:
                    return min(dp(index,0,cost+1),dp(index,indexring-1,cost+1))
                else:
                    return min(dp(index,indexring+1,cost+1),dp(index,indexring-1,cost+1))
        return dp(0,0,0)
obj=Solution()
print(obj.findRotateSteps("godding","gd"))
