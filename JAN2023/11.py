#attempt1: A vertex can be apple or any of its children can be apples
#if this or child is apple, we need to optimistically make the edge between
#this vertex and its parent as +2. Later on, we can subtract for 0
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = {}
        for vertex1, vertex2 in edges:
            if vertex1 not in graph:
                graph[vertex1] =[]
            if vertex2 not in graph:
                graph[vertex2] =[]
            graph[vertex1].append(vertex2)
            graph[vertex2].append(vertex1)
        edges = [0]
        
        def findAllAppleEdges(currentVertex, visited):
            ans = hasApple[currentVertex]
            ansChild = False
            for childVertex in graph[currentVertex]:
                if childVertex not in visited:
                    visited.add(childVertex)
                    ansChild = findAllAppleEdges(childVertex, visited) or ansChild
            if ansChild or ans:
                edges[0] += 2
            #print(currentVertex, ans, ansChild, edges)
            return ans or ansChild

        ans = findAllAppleEdges(0,{0})
        return edges[0] - (2 if ans else 0)
            
