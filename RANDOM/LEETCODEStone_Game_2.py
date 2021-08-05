#attempt1: We only need to track the values accumulated by alex
#We maximize cursum-recurse(call),
#what we need to do for: not taking is minimize the call as we are only concerned
#about the negative part there

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        end=len(piles)
        @lru_cache(None)
        def recurse(start,m,shouldtakeornot):
            if start>=end:
                return 0
            ans=float('inf')
            if shouldtakeornot:
                ans=-float('inf')
            cursum=0
            for i in range(start,min(end,start+2*m)):
                cursum+=piles[i]
                if shouldtakeornot:
                    ans=max(ans,cursum+recurse(i+1,max(m,i-start+1),0))
                else:
                    ans=min(ans,recurse(i+1,max(m,i-start+1),1))
            return ans
        return recurse(0,1,1)
        
            
            
        