#attempt1: TOOK HINT about DJIKSTRA
#Idea is to have Djikstra such that you visit each vertex once
#Where the cost is cnt 
#dont forget to add costa-1 if parent is already visited
from heapq import heappush, heappop
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph={}
        
        for u,v,c in edges:
            if u not in graph:
                graph[u]={}
            if v not in graph:
                graph[v]={}
            graph[u][v]=c
            graph[v][u]=c

        if 0 not in graph:
            return 1

        #print(graph)
        djikstra=[]
        heappush(djikstra,(0,0,0))
        ans=0
        visited=set()
        while(djikstra):
            #print(djikstra,ans,graph)
            cost,parent,costa = heappop(djikstra)
            if parent in visited:
                ans+=costa-1#very important as middle ones can be visited
                continue
            ans+=costa
            visited.add(parent)
            for child in graph[parent]:
                if child not in visited:
                    if cost+graph[parent][child]+1<=maxMoves:
                        heappush(djikstra,(cost+graph[parent][child]+1,child,graph[parent][child]+1))
                        graph[child][parent]=0
                    else:
                        ans+=maxMoves-cost
                        graph[child][parent]-=maxMoves-cost
                else:
                    ans+=min(maxMoves-cost,graph[parent][child])
            #print(parent,ans)
            #print()
        return ans+1