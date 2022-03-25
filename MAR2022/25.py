#attempt1:
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        @lru_cache(None)
        def finder(index,alloted_a,alloted_b):
            if index == 2*n:
                return 0
            if alloted_a == n:
                return sum([costs[i][1] for i in range(index,2*n)])
            if alloted_b == n:
                return sum([costs[i][0] for i in range(index,2*n)])
            return min(finder(index+1,alloted_a+1,alloted_b)+costs[index][0],finder(index+1,alloted_a,alloted_b+1)+costs[index][1])
        return finder(0,0,0)
        
