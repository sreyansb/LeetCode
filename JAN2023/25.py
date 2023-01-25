#attempt2:
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = {}
        for index,edgeVertex in enumerate(edges):
            if edgeVertex != -1:
                graph[index] = edgeVertex
        def bfs(startVertex):
            queue = deque([(startVertex,0)])
            di = {startVertex:0}
            while(queue):
                vertex,steps = queue.popleft()
                if vertex in graph and graph[vertex] not in di:
                    queue.append((graph[vertex],steps+1))
                    di[graph[vertex]] = steps+1
            return di
        di1,di2 = bfs(node1),bfs(node2)
        print(di1,di2)
        ans = float('inf')
        finans = -1
        for key in di1:
            if key in di2:
                ansHere = max(di1[key],di2[key])
                if ansHere < ans:
                    ans = ansHere
                    finans = key
                if ansHere == ans:
                    finans = min(finans,key)
        return finans

#attempt1: WA because you have to return min key
'''
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = {}
        for index,edgeVertex in enumerate(edges):
            if edgeVertex != -1:
                graph[index] = edgeVertex
        def bfs(startVertex):
            queue = deque([(startVertex,0)])
            di = {startVertex:0}
            while(queue):
                vertex,steps = queue.popleft()
                if vertex in graph and graph[vertex] not in di:
                    queue.append((graph[vertex],steps+1))
                    di[graph[vertex]] = steps+1
            return di
        di1,di2 = bfs(node1),bfs(node2)
        print(di1,di2)
        ans = float('inf')
        finans = -1
        for key in di1:
            if key in di2:
                ansHere = max(di1[key],di2[key])
                if ansHere < ans:
                    ans = ansHere
                    finans = key
        return finans
'''
