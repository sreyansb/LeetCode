#attempt1: COPIED DIRECTLY FROM PREVIOUS SUBMISSION
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
                    if len(graph[i])==1:
                        newleaves.append(i)
                #graph[j]=[]
            leaves=newleaves
        return leaves
        
        
