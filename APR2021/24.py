#attempt1: TOOK HELP
#based on CUT EDGES a.k.A bridges
#called as Tarjan's algo
#see https://cp-algorithms.com/graph/bridge-searching.html
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph={}
        for i in connections:
            if i[0] not in graph:
                graph[i[0]]=[]
            if i[1] not in graph:
                graph[i[1]]=[]
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        tin=[-1 for i in range(n)]
        low=[-1 for i in range(n)]
        visited=[False for i in range(n)]
        times=[0]
        ans=[]
        
        def dfs(cur,par=-1):
            visited[cur]=True
            low[cur]=tin[cur]=times[0]
            times[0]+=1
            
            for child in graph[cur]:
                if par==child:
                    continue
                if visited[child]:
                    low[cur]=min(low[cur],tin[child])
                else:
                    dfs(child,cur)
                    low[cur]=min(low[cur],low[child])
                    if low[child]>tin[cur]:
                        ans.append([child,cur])
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        return ans
                        
        
