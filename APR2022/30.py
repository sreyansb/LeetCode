#attempt1:
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        n = len(equations)
        for index in range(n):
            vertex1,vertex2 = equations[index]
            if vertex1 not in graph:
                graph[vertex1] = {}
            if vertex2 not in graph:
                graph[vertex2] = {}
            graph[vertex1][vertex2] = values[index]
            graph[vertex2][vertex1] = 1/values[index]
        visited = set()
        @lru_cache(None)
        def dfs(currentvertex,vertex2,currentans):
            ans = -1
            for next_vertex in graph[currentvertex]:
                if next_vertex == vertex2:
                    return currentans*graph[currentvertex][next_vertex]
                if next_vertex not in visited:
                    visited.add(next_vertex)
                    ans = dfs(next_vertex,vertex2,currentans*graph[currentvertex][next_vertex])
                    if ans != -1:
                        break
            return ans
                    
        ans = []
        for vertex1,vertex2 in queries:
            if vertex1 not in graph or vertex2 not in graph:
                ans.append(-1)
            elif vertex1 == vertex2:
                ans.append(1)
            else:
                visited = set()
                visited.add(vertex1)
                ans.append(dfs(vertex1,vertex2,1))
        return ans
                
            
        
