#attempt1: TOOK HINT
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        graph = {}
        for i in range(n):
            graph[i] = []
        min_string = [i for i in s]
        for index1,index2 in pairs:
            graph[index1].append(index2)
            graph[index2].append(index1)
        
        def find_connected_components(vertex,visited):
            if vertex in visited:
                return
            visited.add(vertex)
            for next_vertex in graph[vertex]:
                find_connected_components(next_vertex,visited)
        
        allvisited = set()
        for i in range(n):
            if i not in allvisited:
                visited = set()
                find_connected_components(i,visited)
                allvisited.update(visited)
                newstr = sorted([s[i] for i in visited])
                index = 0
                for i in sorted(visited):
                    min_string[i] = newstr[index]
                    index += 1
        return "".join(min_string)
        
        
