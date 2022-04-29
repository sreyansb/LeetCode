#attempt2: Used colouring approach
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colours = [-1 for i in range(n)]
        visited = set()
        def colour_graph(vertex,current_colour):
            visited.add(vertex)
            ans = True
            for children in graph[vertex]:
                if colours[children] != -1:
                    if colours[children] != current_colour^1:
                        return False
                else:
                    colours[children] = current_colour^1
                if children not in visited:
                    ans = colour_graph(children,current_colour^1)
                if ans == False:
                    break
            return ans
        ans = True
        for vertex in range(n):
            if colours[vertex] == -1:
                colours[vertex] = 0
                ans = colour_graph(vertex,0)
                if ans == False:
                    break
        return ans
        
                
                

#attempt1: WA because didn't think of Colouring Approach. Always use Colouring Approach
'''
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = set()
        def dfs(vertex,expected_group0,expected_group1,whichgroup):
            visited.add(vertex)
            if whichgroup == 0:
                expected_group1.union(set(graph[vertex]))
                for next_vertex in graph[vertex]:
                    if next_vertex in expected_group0:
                        return False
                    if next_vertex not in visited:
                        ans = dfs(next_vertex,expected_group0,expected_group1,1)
                        if not ans:
                            return False
                    
            else:
                expected_group0.union(set(graph[vertex]))
                for next_vertex in graph[vertex]:
                    if next_vertex in expected_group1:
                        return False
                    if next_vertex not in visited:
                        ans = dfs(next_vertex,expected_group0,expected_group1,0)
                        if not(ans):
                            return False
            return True
        ans = True
        expected_0 = set()
        expected_1 = set()
        for vertex in range(n):
            if vertex not in visited:
                expected_0.add(vertex)
                ans = dfs(vertex,expected_0,expected_1,0)
                if ans == False:
                    return False
        if expected_0&expected_1:
            return False
        return True
                        
            
'''
