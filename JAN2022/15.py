#attempt3: BFS : You make the di_val_index[value] = set() so that same indices
#are not added again
from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        di_val_index = {}
        n = len(arr)
        
        if n==1:
            return 0
        
        for i in range(n):
            if arr[i] not in di_val_index:
                di_val_index[arr[i]] = set()
            di_val_index[arr[i]].add(i)
                
        queue = deque([])
        queue.append((0,1))
        visited = {0}
        while(queue):
            curvertex,count = queue.popleft()
            if curvertex == n-1:
                return count - 1
            allowed = (di_val_index[arr[curvertex]] | {curvertex-1,curvertex+1}) - {curvertex,-1,n}
            for nextindex in allowed:
                if nextindex not in visited:
                    visited.add(nextindex)
                    queue.append((nextindex,count+1))
            di_val_index[arr[curvertex]] = set()
        return -1

#attempt2: BFS : TLE : I dont know why I forget BFS
'''
from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        di_val_index = {}
        n = len(arr)
        
        if n==1:
            return 0
        
        for i in range(n):
            if arr[i] not in di_val_index:
                di_val_index[arr[i]] = set()
            di_val_index[arr[i]].add(i)
        
        graph = {}
        for index in range(1,n-1):
            graph[index] = (di_val_index[arr[index]] | {index-1,index+1}) - {index}
        graph[0] = (di_val_index[arr[0]] | {1}) - {0}
        graph[n-1] = (di_val_index[arr[n-1]] | {n-2}) - {n-1}
        
        queue = deque([])
        queue.append((0,{0}))
        visited = {0}
        while(queue):
            curvertex,curvisited = queue.popleft()
            if curvertex == n-1:
                return len(curvisited) - 1
            for nextindex in graph[curvertex]:
                if nextindex not in visited:
                    visited.add(nextindex)
                    queue.append((nextindex,curvisited|{nextindex}))
        return -1
'''

#attempt1: TLE - DFS
'''
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        di_val_index = {}
        n = len(arr)
        
        if n==1:
            return 0
        
        for i in range(n):
            if arr[i] not in di_val_index:
                di_val_index[arr[i]] = set()
            di_val_index[arr[i]].add(i)
        
        def finder(index,visited):
            #print(index,visited)
            all_allowed = di_val_index[arr[index]]
            #visited.add(index)
            fin = {index-1,index+1}
            if -1 in fin:
                fin.remove(-1)
            all_allowed = (all_allowed|fin) - visited - {index}
            #print(index,all_allowed)
            if n-1 in all_allowed:
                return 1
            ans = n-1-index
            for i in all_allowed:
                ans = min(ans,1+finder(i,visited|{index}))
            #visited.remove(index)
            return ans
        
        return finder(0,set())
'''
