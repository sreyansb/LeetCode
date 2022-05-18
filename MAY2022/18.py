#attempt1:
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
        
        visited=[False for i in range(n)]
        tin=[float('inf') for i in range(n)]
        low=[float('inf') for i in range(n)]
        times=[0]
        ans=[]
        
        def dfs(cur,par=-1):
            visited[cur]=True
            tin[cur]=low[cur]=times[0]
            times[0]+=1
            for child in graph[cur]:
                if child==par:
                    continue
                if visited[child]:
                    low[cur]=min(low[cur],low[child])
                else:
                    dfs(child,cur)
                    low[cur]=min(low[cur],low[child])
                    if low[child]>tin[cur]:
                        ans.append([cur,child])
        
        for i in range(n):
            if not(visited[i]):
                dfs(i)
        
        return ans
                    
            
