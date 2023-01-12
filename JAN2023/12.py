#attempt1:
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = {}
        for vertex1, vertex2 in edges:
            if vertex1 not in graph:
                graph[vertex1] = set()
            if vertex2 not in graph:
                graph[vertex2] = set()
            graph[vertex1].add(vertex2)
            graph[vertex2].add(vertex1)
        ans = [0 for i in range(n)]
        def dfs(currentVertex, visited):
            finalDict = {labels[currentVertex]: 1}
            #print(currentVertex, finalDict)
            for childVertex in graph[currentVertex]:
                if childVertex not in visited:
                    visited.add(childVertex)
                    childDict = dfs(childVertex, visited)
                    for key in childDict:
                        if key not in finalDict:
                            finalDict[key] = 0
                        finalDict[key] += childDict[key]
                    #print(currentVertex, childVertex, finalDict)
            #print(currentVertex,finalDict)
            ans[currentVertex] = finalDict[labels[currentVertex]]
            return finalDict
        dfs(0,{0})
        return ans
        
