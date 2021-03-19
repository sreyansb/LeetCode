#attempt1: Very fast

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        queue=[0]
        while(queue):
            nexty=[]
            for i in queue:
                visited.add(i)
                for j in rooms[i]:
                    if j not in visited:
                        nexty.append(j)
            queue=nexty.copy()
        return len(visited)==len(rooms)
