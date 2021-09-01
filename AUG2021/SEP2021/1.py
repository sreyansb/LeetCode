#attempt1&2: Made a silly mistake in attempt1, changed in 2.
#Can be made faster using arrays instead of sets
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        #run a dfs from unvisited vertices
        n=len(nums)
        allvisited=set()
        maxset=0
        def dfs(index,visited):
            if nums[index] in visited:
                return
            visited.add(nums[index])
            dfs(nums[index],visited)
        for i in range(n):
            if nums[i] not in allvisited:
                visited=set()
                dfs(i,visited)
                maxset=max(maxset,len(visited))
                allvisited=allvisited|visited
        return maxset
                
            
        