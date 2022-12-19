#attempt3:
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        vertex_to_edges = {}
        for vertex1,vertex2 in edges:
            if vertex1 not in vertex_to_edges:
                vertex_to_edges[vertex1] = []
            if vertex2 not in vertex_to_edges:
                vertex_to_edges[vertex2] = []
            vertex_to_edges[vertex1].append(vertex2)
            vertex_to_edges[vertex2].append(vertex1)
        def find_path(source, dest):
            visited = {source}
            queue = deque([source])
            while(queue):
                vertex = queue.popleft()
                for next_vertex in vertex_to_edges[vertex]:
                    if next_vertex == dest:
                        return True
                    if next_vertex in visited:
                        continue
                    visited.add(next_vertex)
                    queue.append(next_vertex)
            return False
        if source not in vertex_to_edges or destination not in vertex_to_edges:
            return source == destination
        return find_path(source, destination)

#attempt2: TLE because forgot to update visited
'''
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        vertex_to_edges = {}
        for vertex1,vertex2 in edges:
            if vertex1 not in vertex_to_edges:
                vertex_to_edges[vertex1] = []
            if vertex2 not in vertex_to_edges:
                vertex_to_edges[vertex2] = []
            vertex_to_edges[vertex1].append(vertex2)
            vertex_to_edges[vertex2].append(vertex1)
        def find_path(source, dest):
            visited = {source}
            queue = deque([source])
            while(queue):
                vertex = queue.popleft()
                for next_vertex in vertex_to_edges[vertex]:
                    if next_vertex == dest:
                        return True
                    if next_vertex in visited:
                        continue
                    queue.append(next_vertex)
            return False
        if source not in vertex_to_edges or destination not in vertex_to_edges:
            return source == destination
        return find_path(source, destination)
'''

#attempt1: Runtime Error because didn't consider the case of vertex not being in graph
'''
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        vertex_to_edges = {}
        for vertex1,vertex2 in edges:
            if vertex1 not in vertex_to_edges:
                vertex_to_edges[vertex1] = []
            if vertex2 not in vertex_to_edges:
                vertex_to_edges[vertex2] = []
            vertex_to_edges[vertex1].append(vertex2)
            vertex_to_edges[vertex2].append(vertex1)
        def find_path(source, dest):
            visited = {source}
            queue = deque([source])
            while(queue):
                vertex = queue.popleft()
                for next_vertex in vertex_to_edges[vertex]:
                    if next_vertex == dest:
                        return True
                    if next_vertex in visited:
                        continue
                    queue.append(next_vertex)
            return False
        return find_path(source, destination)
'''
