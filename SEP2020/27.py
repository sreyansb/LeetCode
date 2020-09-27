#attempt1 : 93.73% and 25%  -> dfs problem, very easy
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph={}#easier for evaluation
        n=len(equations)
        
        #graph creation
        for i in range(n):
            fro,to=equations[i][0],equations[i][1]
            if fro not in graph:
                graph[fro]=[(1.0,fro)]
            if to not in graph:
                graph[to]=[(1.0,to)]
            graph[fro].append((values[i],to))
            graph[to].append((1/values[i],fro))
        
        def dfs(fro,to,visited,answer):
            if fro in visited:
                return -1
            if fro not in graph:
                return -1
            if fro==to:
                return answer
            visited.append(fro)
            ans=-1
            for i in graph[fro]:
                if i[1] not in visited:
                    ans=dfs(i[1],to,visited,answer*i[0])
                    if ans!=-1:
                        return ans
            visited.pop()
            return -1
        
        ans=[]
        for i in queries:
            fro,to=i[0],i[1]
            ans.append(dfs(fro,to,[],1))
        return ans
            
        
