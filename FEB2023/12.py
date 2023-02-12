#attempt1: Took HELP
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for c1,c2 in roads:
            graph[c1].append(c2)
            graph[c2].append(c1)
        res = [0]

        def dfs(node,par):
            totalPeople = 1
            for nei in graph[node]:
            	if nei != par:
                    people, car = dfs(nei,node)
                    totalPeople += people
                    res[0] += car
            cars = ceil(totalPeople/seats) 
            return totalPeople,cars

        dfs(0,None)
        return res[0]
