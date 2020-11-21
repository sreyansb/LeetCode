#attempt3: 70%
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n=len(nums)
        visited=[0 for i in range(n)]
        def connected(index,number):
            #print(index,number,visited)
            if visited[nums[index]]:
                return number
            visited[nums[index]]=1
            return connected(nums[index],number+1)
        lengths=[]
        for i in range(n):
            if not(visited[i]):
                l=connected(i,0)
                #allvisited=allvisited|visited
                lengths.append(l)
                #print(lengths)
        return max(lengths)

#attempt2: very easy problem dfs based
'''
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n=len(nums)
        def connected(index,number,visited):
            #print(index,number,visited)
            if nums[index] in visited:
                return number
            visited.add(nums[index])
            return connected(nums[index],number+1,visited)
        allvisited=set()
        lengths=[]
        for i in range(n):
            if i not in allvisited:
                l=connected(i,0,allvisited)
                #allvisited=allvisited|visited
                lengths.append(l)
                #print(lengths)
        return max(lengths)
'''

#attempt 1:
'''
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n=len(nums)
        def connected(index,number,visited):
            #print(index,number,visited)
            if nums[index] in visited:
                return number
            visited.add(nums[index])
            return connected(nums[index],number+1,visited)
        allvisited=set()
        lengths=[]
        for i in range(n):
            if i not in allvisited:
                visited=set()
                l=connected(i,0,visited)
                allvisited=allvisited|visited
                lengths.append(l)
                #print(lengths)
        return max(lengths)
'''
