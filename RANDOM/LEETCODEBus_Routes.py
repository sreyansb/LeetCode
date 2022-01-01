#attempt4: AC
from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        
        bus_stations = len(routes)
        stations_to_bus = {}
        for routeindex in range(bus_stations):
            
            route = routes[routeindex]
            #routes[routeindex] = set(routes[routeindex])
            for station in route:
                if station not in stations_to_bus:
                    stations_to_bus[station] = set()
                stations_to_bus[station].add(routeindex)
        
        if target not in stations_to_bus:
            return -1
        
        ans = [float('inf')]
        
        def findpath(curstation,curroute,visited):
            queue = deque([])
            queue.append((curroute,curstation,visited))
            while(queue):
                #print(queue)
                route,station,visitedtillhere = queue.popleft()
                
                if route in stations_to_bus[target]:
                    ans[0] = min(ans[0],len(visitedtillhere)+1)
                    break
                
                for each_station in routes[route]:
                    for next_route in stations_to_bus[each_station]:
                        if next_route!=route and next_route not in visitedtillhere:
                            queue.append((next_route,each_station,visitedtillhere|{route}))          
            return
                
        for startroute in stations_to_bus[source]:
            findpath(source,startroute,set())
        
        return ans[0] if ans[0]!=float('inf') else -1

#attempt3: TRIED BFS
#RunTime Error : KeyError because target might not be a station in any route
'''
from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        
        bus_stations = len(routes)
        stations_to_bus = {}
        for routeindex in range(bus_stations):
            
            route = routes[routeindex]
            #routes[routeindex] = set(routes[routeindex])
            for station in route:
                if station not in stations_to_bus:
                    stations_to_bus[station] = set()
                stations_to_bus[station].add(routeindex)
        
        ans = [float('inf')]
        
        def findpath(curstation,curroute,visited):
            queue = deque([])
            queue.append((curroute,curstation,visited))
            while(queue):
                #print(queue)
                route,station,visitedtillhere = queue.popleft()
                
                if route in stations_to_bus[target]:
                    ans[0] = min(ans[0],len(visitedtillhere)+1)
                    break
                
                for each_station in routes[route]:
                    for next_route in stations_to_bus[each_station]:
                        if next_route!=route and next_route not in visitedtillhere:
                            queue.append((next_route,each_station,visitedtillhere|{route}))          
            return
                
        for startroute in stations_to_bus[source]:
            findpath(source,startroute,set())
        
        return ans[0] if ans[0]!=float('inf') else -1        
'''

#attempt2: TLE because I was using DFS
'''
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        bus_stations = len(routes)
        #bus_to_stations = routes
        stations_to_bus = {}
        for routeindex in range(bus_stations):
            
            route = routes[routeindex]
            routes[routeindex] = set(routes[routeindex])
            for station in route:
                if station not in stations_to_bus:
                    stations_to_bus[station] = set()
                stations_to_bus[station].add(routeindex)
        
        ans = [float('inf')]
        def findpath(curstation,curroute,visited):
            
            if curroute in visited:
                return
            
            if target in routes[curroute]:
                ans[0] = min(ans[0],len(visited)+1)
                return
                
            for nextstation in routes[curroute]:
                for other_route in stations_to_bus[nextstation]:
                    if curroute != other_route:
                        findpath(nextstation,other_route,visited|{curroute})
        
        
        
        for startroute in stations_to_bus[source]:
            findpath(source,startroute,set())
        
        return ans[0] if ans[0]!=float('inf') else -1        
'''

#attempt1: WA because if source==target then answer has to be 0
'''
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        bus_stations = len(routes)
        #bus_to_stations = routes
        stations_to_bus = {}
        for routeindex in range(bus_stations):
            
            route = routes[routeindex]
            routes[routeindex] = set(routes[routeindex])
            for station in route:
                if station not in stations_to_bus:
                    stations_to_bus[station] = set()
                stations_to_bus[station].add(routeindex)
        
        ans = [float('inf')]
        def findpath(curstation,curroute,visited):
            
            if curroute in visited:
                return
            
            if target in routes[curroute]:
                ans[0] = min(ans[0],len(visited)+1)
                return
                
            for nextstation in routes[curroute]:
                for other_route in stations_to_bus[nextstation]:
                    if curroute != other_route:
                        findpath(nextstation,other_route,visited|{curroute})
        
        for startroute in stations_to_bus[source]:
            findpath(source,startroute,set())
        
        return ans[0] if ans[0]!=float('inf') else -1        
'''
