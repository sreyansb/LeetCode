#Attempt-3 took help
class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        visited=[0 for i in range(days[-1]+1)]
        for i in range(days[-1]+1):
            if i not in days:
                visited[i]=visited[i-1]
            else:
                visited[i]=min(visited[max(0,i-1)]+cost[0],visited[max(0,i-7)]+cost[1],visited[max(0,i-30)]+cost[2])
        return visited[days[-1]]

"""
#Attempt 2
#gave WA->couldn't debug
def recur(i,visited,costs,n,dp,co=0):
    if i>n:
        return co
    
    if dp[i]!=-1:
        return dp[i]
    
    if visited[i]==0:
        dp[i] = recur(i+1,visited,costs,n,dp,co)
        return dp[i]
    dp[i]=min(recur(i+1,visited,costs,n,dp,co+costs[0]),recur(i+7,visited,costs,n,dp,co+costs[1]),recur(i+30,visited,costs,n,dp,co+costs[2]))
    return dp[i]


class Solution:
    def mincostTickets(self, days, costs):
        visited=[0]*366
        for i in days:
            visited[i]=1
        dp=[-1 for _ in range(366)]
        return(recur(days[0],visited,costs,days[-1],dp))

obj=Solution()
print(obj.mincostTickets([1,4,6,7,8,20],[2,7,15]))
"""

"""
#Attempt 1:TLE
from math import inf
def recur(i,visited,costs,n,co=0):
    if i>n:
        return co
    if visited[i]==0:
        return recur(i+1,visited,costs,n,co)
    return min(recur(i+1,visited,costs,n,co+costs[0]),recur(i+7,visited,costs,n,co+costs[1]),recur(i+30,visited,costs,n,co+costs[2]))
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        visited=[0]*366
        for i in days:
            visited[i]=1
        cost=inf
        return recur(days[0],visited,costs,days[-1])
"""
