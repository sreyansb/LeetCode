#attempt1:
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evens = 0
        odds = 0
        for i in position:
            if i&1:
                odds += 1
            else:
                evens += 1
        return min(odds,evens)
        
