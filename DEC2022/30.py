#attempt1:
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        newGraph = {}
        for index in range(n):
            newGraph[index] = []
            for nextIndex in graph[index]:
                newGraph[index].append(nextIndex)
        @lru_cache(None)
        def findPaths(currentVertex):
            if currentVertex == n-1:
                return {tuple((n-1,))}
            ans = set()
            for nextVertex in newGraph[currentVertex]:
                newVertexPaths = findPaths(nextVertex)
                print(newVertexPaths)
                for newVertexPath in newVertexPaths:
                    print(newVertexPath)
                    if n-1 in newVertexPath:
                        ans.add(tuple((currentVertex,)) + newVertexPath)
            return ans
        return findPaths(0)
            
        
