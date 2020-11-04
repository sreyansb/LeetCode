#attempt2: took help 86%.
#atmost two nodes can give MHT, so it is better to have a toposort of a problem
#remove all nodes with 1 connection such that at most 2 nodes remain
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        graph=[[] for i in range(n)]
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        leaves=[i for i in range(n) if len(graph[i])==1]
        while(n>2):
            #print(leaves)
            n-=len(leaves)
            newleaves=[]
            for j in leaves:
                for i in graph[j]:
                    graph[i].remove(j)
                    if len(graph[i])==1:#has to be here 
                        newleaves.append(i)
                #graph[j]=[]
            leaves=newleaves
        return leaves

#attempt1: TLE 60/68 -> dfs on each vertex of the graph
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        height=[1 for i in range(n)]
        heights=[0 for i in range(n)]
        graph=[[] for i in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        def dfs(vertex,visited):
            if vertex in visited:
                return 0
            maxi=0
            visited.add(vertex)
            for i in graph[vertex]:
                maxi=max(maxi,dfs(i,visited))
            height[vertex]+=maxi
            return height[vertex]
        for i in range(n):
            heights[i]=dfs(i,set())
            height=[1 for i in range(n)]
        minh=min(heights)
        ans=[]
        for i in range(n):
            if heights[i]==minh:
                ans.append(i)
        return ans
"""
