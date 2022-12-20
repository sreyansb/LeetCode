#attempt1:
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        def bfs():
            queue = deque([0])
            visited = {0}
            while(queue):
                currentRoom = queue.popleft()
                for nextRoom in rooms[currentRoom]:
                    if nextRoom not in visited:
                        visited.add(nextRoom)
                        queue.append(nextRoom)
            return len(visited)
        return bfs() == n
