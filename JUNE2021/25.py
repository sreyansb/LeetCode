#attempt1: Remove all the required edges (Tarjan's Algo) from the list of given edges
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #all edges - cut edges? =>tarjan's algo
        times=[0]
        n=len(edges)
        low=[float('inf') for i in range(n+1)]
        tin=[float('inf') for i in range(n+1)]
        ans=set()
        visited=[0 for i in range(n+1)]
        graph={}
        for i in edges:
            if i[0] not in graph:
                graph[i[0]]=[]
            if i[1] not in graph:
                graph[i[1]]=[]
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        def tarjan(cur,parent):
            visited[cur]=1
            low[cur]=tin[cur]=times[0]
            times[0]+=1
            for child in graph[cur]:
                if child==parent:
                    continue
                if visited[child]:
                    low[cur]=min(low[cur],tin[child])
                else:
                    tarjan(child,cur)
                    low[cur]=min(low[cur],low[child])
                    if low[child]>tin[cur]:
                        ans.add((cur,child))
                        ans.add((child,cur))
        tarjan(1,-1)
        edges={tuple(edges[i]):i for i in range(n)}
        for i in ans:
            if i in edges:
                del edges[i]
        parent=None
        for i in edges:
            parent=i
        return list(parent)