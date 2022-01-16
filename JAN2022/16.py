#attempt1:
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)#thi
        dist = [float('inf') for i in range(n)]
        
        for i in range(n):
            if seats[i]:
                dist[i] = 0
            else:
                dist[i] = dist[i-1] + 1 if i-1>=0 else float('inf')
        
        for i in range(n-2,-1,-1):
            if seats[i]:
                dist[i] = 0
            else:
                dist[i] = min(dist[i],dist[i+1] + 1)
        
        return max(dist)
        
