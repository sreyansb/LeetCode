#attempt2: we get the max height to the right and max height to the left and
#then check the difference w.r.t. 0
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxrights=[height[-1] for i in range(n)]
        for i in range(n-2,-1,-1):
            maxrights[i] = max(height[i],maxrights[i+1])
        maxlefts=[height[0] for i in range(n)]
        for i in range(1,n):
            maxlefts[i]=max(maxlefts[i-1],height[i])
        ans=0
        for i in range(n):
            ans+=max(0,min(maxleft[i]-height[i],maxrights[i]-height[i]))
        return ans

#attempt1:
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxrights = [height[-1] for i in range(n)]
        for i in range(n-2,-1,-1):
            maxrights[i] = max(height[i],maxrights[i+1])
        maxleft=0
        ans=0
        for i in range(n):
            ans+=max(0,min(maxleft-height[i],maxrights[i]-height[i]))
            maxleft=max(maxleft,height[i])
        return ans
        
        
"""
        
