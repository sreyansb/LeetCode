#attempt2: 91% and 90% Using heap and MST concept
from heapq import heappush,heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        number_of_points = len(points)
        cost = 0
        heap = []
        unvisited = set(range(1,number_of_points))
        for i in unvisited:
            distance = abs(points[0][0]-points[i][0]) + abs(points[0][1]-points[i][1])
            heappush(heap,(distance,i))
        while(unvisited):
            while(heap[0][1] not in unvisited):
                heappop(heap)
            mindistance,unvisited_index = heappop(heap)
            cost += mindistance
            unvisited.remove(unvisited_index)
            for i in unvisited:
                distance = abs(points[unvisited_index][0]-points[i][0]) + abs(points[unvisited_index][1]-points[i][1])
                heappush(heap,(distance,i))
            
        return cost
                    
        


#attempt1: TLE because of O(n^2)
'''
from sortedcontainers import SortedList
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        number_of_points = len(points)
        visited = set()
        cost = 0
        visited.add(0)
        unvisited = set(range(1,number_of_points))
        while(unvisited):
            min_distance,end_vertex = float('inf'),-1
            for visited_index in visited:
                for unvisited_index in unvisited:
                    distance = abs(points[visited_index][0]-points[unvisited_index][0]) + abs(points[visited_index][1]-points[unvisited_index][1])
                    if distance < min_distance:
                        min_distance = distance
                        end_vertex = unvisited_index
            visited.add(end_vertex)
            cost += min_distance
            unvisited.remove(end_vertex)
        return cost
                    
        
'''
