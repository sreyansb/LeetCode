#attempt1:
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [float('inf')]*n
        #0 is red and 1 is blue
        graph = {0:{},1:{}}
        def makeGraphFromEdges(edgeColor, edgeList):
            for a,b in edgeList:
                if a not in graph[edgeColor]: 
                    graph[edgeColor][a] = set()
                graph[edgeColor][a].add(b)
        makeGraphFromEdges(0,redEdges)
        makeGraphFromEdges(1,blueEdges)
        queue = deque([])
        visited = set()
        queue.append((0,0,0))
        queue.append((0,0,1))
        #print(graph)
        while(queue):
            #print(queue)
            vertex,steps,edgeColor = queue.popleft()
            ans[vertex] = min(ans[vertex],steps)
            visited.add((vertex,edgeColor))
            nextColor = edgeColor ^ 1
            if vertex not in graph[nextColor]:
                continue
            for nextVertex in graph[nextColor][vertex]:
                if (nextVertex, nextColor) in visited:
                    continue
                queue.append((nextVertex, steps+1, nextColor))
            
        for index, val in enumerate(ans):
            if val == float('inf'):
                ans[index] = -1
        return ans
