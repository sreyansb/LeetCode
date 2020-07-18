def iscyclic(graph,i,visited,stac):
    visited[i]=1
    stac[i]=1
    for j in graph[i]:
        if visited[j]==0:
            if iscyclic(graph,j,visited,stac):
                return True 
        elif stac[j]:
            return True
    stac[i]=0
    return False

def checkcycle(graph,numCourses):
    visited=[0]*numCourses
    stac=[0]*numCourses
    for i in range(numCourses):
        if not visited[i]:
            if iscyclic(graph,i,visited,stac):
                return True
    return False
        
    
def toposort(graph,i,visited,final):
    visited[i]=1
    for j in graph[i]:
            if not visited[j]:
                toposort(graph,j,visited,final)
    final.append(i)
            
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for i in range(numCourses)]
        for i in prerequisites:
            graph[i[1]].append(i[0])
        if checkcycle(graph,numCourses):
            return []
        final=[]
        visitedi=[0]*numCourses
        visited=[0]*numCourses
        for i in range(numCourses):
                if not visited[i]:
                    toposort(graph,i,visited,final)
        return final[::-1]
        
        
                
            
        
