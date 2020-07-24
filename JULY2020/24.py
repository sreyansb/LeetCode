def findpath(graph,ini,fin,visited,res):
    if ini==fin:
        #print(ini,visited)
        res.append(visited.copy())
        return
    for i in graph[ini]:
        visited.append(i)
        findpath(graph,i,fin,visited,res)
        visited.pop()
class Solution:
    def allPathsSourceTarget(self, graph):
        res=[]
        visited=[0]
        findpath(graph,0,len(graph)-1,visited,res)
        return res
obj=Solution()
print(obj.allPathsSourceTarget([[1,2], [3], [3], []] ))
