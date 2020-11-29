#aattempt2: all visited indices are marked negative
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        def dfs(index):
            if index>=n:
                return False
            if index<0:
                return False
            if arr[index]<0:
                return False
            if arr[index]==0:
                return True
            arr[index]*=-1
            return dfs(index-arr[index]) or dfs(index+arr[index])
        return dfs(start)
    
#attempt1: 31% and 20%
'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        def dfs(index,visited):
            if index>=n:
                return False
            if index<0:
                return False
            if index in visited:
                return False
            if arr[index]==0:
                return True
            visited.append(index)
            return dfs(index-arr[index],visited) or dfs(index+arr[index],visited)
        return dfs(start,[])
'''
