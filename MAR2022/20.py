#attempt1:
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        available_options = set(range(1,7))
        n = len(tops)
        for i in range(n):
            available_options = available_options&{tops[i],bottoms[i]}
            if not(available_options):
                return -1
        minswaps = float('inf')
        for i in available_options:
            noswaps1 = 0
            noswaps2 = 0
            for j in range(n):
                if tops[j] != i:
                    noswaps1 += 1
                if bottoms[j] != i:
                    noswaps2 += 1
            minswaps = min(minswaps,noswaps1,noswaps2)
        return minswaps
            
            
