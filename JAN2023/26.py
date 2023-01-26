#attempt7: TOOK HELP: had similar approach: but you need to keep visited for 
#city and k
from collections import defaultdict
from heapq import heappop,heappush
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for v1,v2,price in flights:
            graph[v1].append((v2,price))
        #print(graph)
        minAns = [float('inf')]
        k += 1
        def bfs(src):
            heap = [(0,0,src)]
            visited = set()
            while(heap):
                price,curK,curSrc = heappop(heap)
                if curSrc == dst:
                    return price
                if (curSrc,curK) in visited or curK+1 > k:
                    continue
                visited.add((curSrc,curK))
                for nextCity,nextPrice in sorted(graph[curSrc], key=lambda x:x[1]):
                    heappush(heap,(price+nextPrice,curK+1,nextCity))
            return -1
        return bfs(src)

#attempt6: WA
'''
from collections import defaultdict
from heapq import heappop,heappush
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for v1,v2,price in flights:
            graph[v1].append((v2,price))
        #print(graph)
        minAns = [float('inf')]
        k += 1
        def bfs(src):
            heap = [(0,0,src,{src})]
            while(heap):
                #print(heap)
                price,curK,curSrc,visited = heappop(heap)
                if curSrc == dst:
                    return price
                visited.add(curSrc)
                for nextCity,nextPrice in sorted(graph[curSrc], key=lambda x:x[1]):
                    if nextCity in visited or curK+1 > k:
                        continue
                    heappush(heap,(price+nextPrice,curK+1,nextCity,visited))
            return -1
        return bfs(src)
'''

#attempt5: Memory Limit Exceeded
'''
from collections import defaultdict
from heapq import heappop,heappush
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for v1,v2,price in flights:
            graph[v1].append((v2,price))
        #print(graph)
        minAns = [float('inf')]
        k += 1
        def bfs(src):
            heap = [(0,0,src,{src})]
            while(heap):
                #print(heap)
                price,curK,curSrc,visited = heappop(heap)
                if curSrc == dst:
                    return price
                visited.add(curSrc)
                for nextCity,nextPrice in sorted(graph[curSrc], key=lambda x:x[1]):
                    if nextCity in visited or curK+1 > k:
                        continue
                    heappush(heap,(price+nextPrice,curK+1,nextCity,visited|{curSrc}))
            return -1
        return bfs(src)
'''

#attempt4: Output Limit Exceeded: Unneccessary prints
'''
from collections import defaultdict
from heapq import heappop,heappush
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for v1,v2,price in flights:
            graph[v1].append((v2,price))
        #print(graph)
        minAns = [float('inf')]
        k += 1
        def bfs(src):
            heap = [(0,0,src,{src})]
            while(heap):
                print(heap)
                price,curK,curSrc,visited = heappop(heap)
                if curSrc == dst:
                    return price
                visited.add(curSrc)
                for nextCity,nextPrice in sorted(graph[curSrc], key=lambda x:x[1]):
                    if nextCity in visited or curK+1 > k:
                        continue
                    heappush(heap,(price+nextPrice,curK+1,nextCity,visited|{curSrc}))
            return -1
        return bfs(src)
'''

#attempt3: WA
'''
from collections import defaultdict
from heapq import heappop,heappush
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for v1,v2,price in flights:
            graph[v1].append((v2,price))
        print(graph)
        minAns = [float('inf')]
        k += 1
        def bfs(src):
            heap = [(0,0,src,{0})]
            while(heap):
                #print(heap)
                price,curK,curSrc,visited = heappop(heap)
                if curSrc == dst:
                    return price
                visited.add(curSrc)
                for nextCity,nextPrice in sorted(graph[curSrc], key=lambda x:x[1]):
                    if nextCity in visited or curK+1 > k:
                        continue
                    heappush(heap,(price+nextPrice,curK+1,nextCity,visited|{curSrc}))
            return -1
        return bfs(src)
'''

#attempt2: WA: tried using heaped BFS
'''
from collections import defaultdict
from heapq import heappop,heappush
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for v1,v2,price in flights:
            graph[v1].append((v2,price))
        minAns = [float('inf')]
        k += 1
        def bfs(src):
            heap = [(0,0,src)]
            visited = {src}
            while(heap):
                #print(heap)
                price,curK,curSrc = heappop(heap)
                if curSrc == dst:
                    return price
                visited.add(curSrc)
                for nextCity,nextPrice in sorted(graph[curSrc], key=lambda x:x[1]):
                    if nextCity in visited or curK+1 > k:
                        continue
                    heappush(heap,(price+nextPrice,curK+1,nextCity))
            return -1
        return bfs(src)
'''

#attempt1: TLE because I used DFS
'''
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for v1,v2,price in flights:
            graph[v1].append((v2,price))
        minAns = [float('inf')]
        k += 1
        def dfs(src,curk,price,visited):
            #print(src,curk,k,price,minAns)
            if src == dst:
                minAns[0] = min(minAns[0],price)
                return
            if price >= minAns[0] or curk >= k:
                return
            for nextVertex,nextPrice in graph[src]:
                if nextVertex not in visited:
                    dfs(nextVertex, curk+1, price+nextPrice,visited|{src})
        dfs(src,0,0,set())
        if minAns[0] == float('inf'):
            minAns[0] = -1
        return minAns[0]
'''
