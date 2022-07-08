#attempt1: TOOK HELP couldn't get a solution
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        @lru_cache(None)
        def dp(houseindex,parentcolor,neighbours):
            
            if (neighbours>target) or (houseindex == m and neighbours!=target):
                return float('inf')
            if houseindex == m:
                return 0
            if houses[houseindex]:
                return dp(houseindex+1,houses[houseindex],neighbours+(houses[houseindex]!=parentcolor))
            ans = float('inf')
            for color in range(1,n+1):
                if color != parentcolor:
                    ans = min(ans,dp(houseindex+1,color,neighbours+1)+cost[houseindex][color-1])
                else:
                    ans = min(ans,dp(houseindex+1,color,neighbours)+cost[houseindex][color-1])
            return ans
        
        ans = dp(0,0,0)
        return -1 if ans == float('inf') else ans
