#attempt2:
from heapq import heappush,heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        graph = {}
        for vertex in range(1,n+1):
            graph[vertex] = {}
        for startvertex,endvertex,weight in times:
            graph[startvertex][endvertex] = weight
        heap = []
        maxweight = -float('inf')
        heappush(heap,(0,k))
        while(heap):
            weight,vertex = heappop(heap)
            if vertex in visited:
                continue
            maxweight = max(maxweight,weight)
            visited.add(vertex)
            for next_vertex in graph[vertex]:
                next_weight = weight+graph[vertex][next_vertex]
                heappush(heap,(next_weight,next_vertex))
        if len(visited) == n:
            return maxweight
        return -1        

#attempt1: WA because it is not shortest distance
'''
from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        graph = {}
        for vertex in range(1,n+1):
            graph[vertex] = {}
        for startvertex,endvertex,weight in times:
            graph[startvertex][endvertex] = weight
        visited.add(k)
        queue = deque([])
        queue.append((k,0))
        maxweight = -float('inf')
        while(queue):
            vertex,weight = queue.popleft()
            for next_vertex in graph[vertex]:
                if next_vertex in visited:
                    continue
                visited.add(next_vertex)
                next_weight = weight+graph[vertex][next_vertex]
                maxweight = max(maxweight,next_weight)
                queue.append((next_vertex,next_weight))
        if len(visited) == n:
            return maxweight
        return -1
'''
        
        
