
#aattempt1:
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp={}
        def findcost(index):
            if index>=n:
                return 0
            if index not in dp:
                dp[index]=cost[index]+min(findcost(index+1),findcost(index+2))
            return dp[index]
        return min(findcost(0),findcost(1))
            
            
