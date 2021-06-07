#attempt3:
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        di={}
        for i in range(9):
            di[cost[i]]=i+1
        visited={}
        def dp(target):
            if target<0:
                return -float('inf')
            if target==0:
                return 0
            if target not in visited:
                ans=-float('inf')
                for i in di:
                    ans=max(ans,di[i]+10*dp(target-i))
                visited[target]=ans
            return visited[target]
        return str(max(0,dp(target)))

#attempt2: TLE
'''
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        maxie=[0]
        di={}
        for i in range(9):
            di[cost[i]]=str(i+1)
        visited=set()
        @lru_cache(None)
        def dp(target,curstr):
            #print(curstr)
            if target<0:
                return
            if curstr in visited:
                return
            visited.add(curstr)
            if target==0:
                maxie[0]=max(maxie[0],int(curstr))
                return
            for i in di:
                if target-i>=0:
                    dp(target-i,curstr+di[i])
        dp(target,"")
        return str(maxie[0])
'''

#attempt1: Memory Issues: Recursion Depth Breached
'''
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        maxie=[0]
        @lru_cache(None)
        def dp(target,curstr):
            if target<0:
                return
            if target==0:
                maxie[0]=max(maxie[0],int(curstr))
                return
            for i in range(9):
                if target-cost[i]>=0:
                    dp(target-cost[i],curstr+str(i+1))
        dp(target,"")
        return str(maxie[0])
'''