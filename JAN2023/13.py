#attempt2:
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        graph = {index:set() for index in range(n)}
        for index, parentVertex in enumerate(parent):
            if index == 0:
                continue
            graph[parentVertex].add(index)
        maxAns = [0]
        maxie = [""]
        def dfs(currentVertex):
            
            childAns = []
            for childVertex in graph[currentVertex]:
                if s[childVertex] == s[currentVertex]:
                    dfs(childVertex)
                else:
                    childAns.append(dfs(childVertex))
            
            ans = sum(sorted(childAns, reverse = True)[:2]) + 1
            maxAns[0] = max(maxAns[0], ans)
            return ans - sum(sorted(childAns, reverse = True)[1:2])
        dfs(0)
        return maxAns[0]
