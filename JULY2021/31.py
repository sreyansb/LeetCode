#attempt1: TOOK HELP
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        n=len(height)
        maxr=[height[-1] for i in range(n)]
        maxl=[height[0] for i in range(n)]
        for i in range(n-2,-1,-1):
            maxr[i]=max(maxr[i+1],height[i])
        for i in range(1,n):
            maxl[i]=max(maxl[i-1],height[i])
        #print(maxl)
        #print(maxr)
        for i in range(n):
            ans+=max(0,min(-(height[i]-maxl[i]),-height[i]+maxr[i]))
        return ans
'''