#attempt1: amazingly easy problem but needed hints
#amazingly worded -> seems like dp but very easy just odd even based
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds=0
        evens=0
        for i in position:
            if i%2:
                odds+=1
            else:
                evens+=1
        return odds if odds<evens else evens
        
