#attempt1:
from sortedcontainers import SortedList
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = SortedList([])
        for row in matrix:
            for ele in row:
                l.add(ele)
        return l[k-1]
    
        
