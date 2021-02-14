#attempt2: TO check if graph is bipartite.
#I first did simple matching to see if there is no link between two child nodes
#of a parent node. I got WA because ones with cycle and odd number of nodes
#is not bipartite.
#So I saw cycle checking part as well
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        graphlen=len(graph)
        matrix=[[0 for i in range(graphlen)] for i in range(graphlen)]
        for i in range(graphlen):
            for j in graph[i]:
                matrix[i][j]=1
            
        for i in range(graphlen):
            for j in range(graphlen):
                for k in range(graphlen):
                    if matrix[i][j] and matrix[i][k] and matrix[j][k]:
                        return False
        visited=[0 for i in range(graphlen)]
        def cycle(index,visited,parent):
            visited[index]=1
            for i in range(graphlen):
                if matrix[index][i]:
                    if visited[i]==0:
                        if cycle(i,visited,index):
                            return True
                    elif i!=parent:
                        return True
            return False
        return False if (cycle(0,visited,-1) and graphlen&1) else True
        
