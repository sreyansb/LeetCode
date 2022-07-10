#attempt2: attempt1 was wrong because of me not using lru_cache or dp
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        @lru_cache(None)
        def findsol(index):
            if index >= n:
                return 0
            return min(findsol(index+1),findsol(index+2))+cost[index]
        return min(findsol(0),findsol(1))
