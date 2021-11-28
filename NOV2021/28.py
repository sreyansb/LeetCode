#attempt3: BFS
from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        queue = deque([])
        queue.append((0,[0]))
        ans = []
        while(queue):
            vert,visi = queue.popleft()
            for i in graph[vert]:
                if i == n-1:
                    ans.append(visi+[n-1])
                    continue
                queue.append((i,visi+[i]))
        return ans

#attempt2: WHY do I forget BFS?!
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        #di = {i:graph[i] for i in range(n)}
        ans = []
        def find(curvertex,visited):
            if curvertex == n-1:
                ans.append(visited.copy())
                return
            for i in graph[curvertex]:
                find(i,visited+[i])
        find(0,[0])
        return ans
'''        
#attempt1:
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        #di = {i:graph[i] for i in range(n)}
        ans = []
        def find(curvertex,visited):
            if curvertex == n-1:
                ans.append(visited.copy())
                return
            for i in graph[curvertex]:
                if i not in visited:
                    find(i,visited+[i])
        find(0,[0])
        return ans
            
        
'''
