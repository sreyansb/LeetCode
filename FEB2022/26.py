#attempt6: TOOK HELP :  ALMOST COPIEDAC
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        reqd_bin_n = (1<<n)-1
        visited_from_node_i = []
        queue = []
        for i in range(n):
            visited_from_node_i.append({1<<i})
            queue.append((1<<i,i))
        path = 0
        while(queue):
            #print(queue)
            path += 1
            newqueue = []
            for visited,pathy in queue:
                for neighbour in graph[pathy]:
                    newele = 1<<neighbour
                    value = visited|newele
                    #visited_from_node_i[neighbour] and not pathy
                    if value not in visited_from_node_i[neighbour]:
                        if value == reqd_bin_n:
                            return path
                        newqueue.append((value,neighbour))
                        visited_from_node_i[neighbour].add(value)
            queue = newqueue
            #print(visited_from_node_i)
        return 0

#attempt5: WA
'''
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        reqd_bin_n = (1<<n)-1
        visited_from_node_i = []
        queue = []
        for i in range(n):
            visited_from_node_i.append({1<<i})
            queue.append((1<<i,i))
        path = 0
        while(queue):
            #print(queue)
            path += 1
            newqueue = []
            for visited,pathy in queue:
                for neighbour in graph[pathy]:
                    newele = 1<<neighbour
                    value = visited|newele
                    if value not in visited_from_node_i[neighbour]:
                        if value == reqd_bin_n:
                            return path
                        newqueue.append((value,neighbour))
                        visited_from_node_i[neighbour].add(value)
            queue = newqueue
            #print(visited_from_node_i)
        return 1
'''

#attempt1,2,3&4 : TLE because of dfs
'''
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        reqd_bin_n = (1<<n)-1
        ans = [float('inf')]
        ans1 = [[]]
        
        dpt = set()
        def dfs(curnode,number_of_steps,unique_nodes):
            
            if unique_nodes == reqd_bin_n:
                ans[0] = min(ans[0],number_of_steps)
                return
            if (curnode,unique_nodes) in dpt:
                return
            if number_of_steps>=ans[0]:
                return
            #newone = {(curnode,unique_nodes)}
            dpt.add((curnode,unique_nodes))
            for i in graph[curnode]:
                if (i,unique_nodes|(1<<i)) not in dpt:
                    dfs(i,number_of_steps+1,unique_nodes|(1<<i))
            dpt.remove((curnode,unique_nodes))
            
        
        for i in range(n):
            dfs(i,0,1<<i)
        return ans[0]
'''



    
                    
        
