#CHECK FOR CYCLE IN A DAG
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

#calling-checkcycle(graph,numCourses)->graph is an adjacency list

def toposort(graph,i,visited,final):
    visited[i]=1
    for j in graph[i]:
        if not visited[j]:
            toposort(graph,j,visited,final)
    final.append(i)

#CALLING toposort
    
'''
visited=[0]*numCourses
final=[]
for i in range(numCourses):
    if not(visited[i]):
        toposort(graph,i,visited,final)
print(final[::-1])
'''




