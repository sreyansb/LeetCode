#Attempt2: Graph Coloring question
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not(dislikes):
            return True
        graph={}
        for i in dislikes:
            if i[0] not in graph:
                graph[i[0]]=[]
            if i[1] not in graph:
                graph[i[1]]=[]
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        visited=[0]*(N+2)
        def colorkaro(vertex,col):
            visited[vertex]=col
            for child in graph[vertex]:
                if visited[child]==col:
                    return False
                elif visited[child]==0 and colorkaro(child,-col)==False:
                    return False
            return True
        for i in range(1,N+1):
            if visited[i]==0 and i in graph and not(colorkaro(i,1)):
                return False
        return True
            
#Attempt1: WA 50/70 - was wrong because 2 vertices having different
#parents might be in same group and hence prduce wrong results.
"""
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        groups=[-1]*(N+1)
        dislikes.sort(key=lambda x:x[0])
        ans=True
        for i in dislikes:
            if groups[i[0]]==-1 and groups[i[1]]==-1:
                groups[i[0]]=0
                groups[i[1]]=1
            elif groups[i[0]]==-1:
                groups[i[0]]=groups[i[1]]^1
            elif groups[i[1]]==-1:
                groups[i[1]]=groups[i[0]]^1
            else:
                if groups[i[0]]==groups[i[1]]:
                    ans=False
                    break
            
        return ans
"""
