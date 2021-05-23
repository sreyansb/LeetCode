#attempt4: BFS

from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[-1 for i in range(n)]
        dp[n-1]=0
        vals={}
        for i in range(n):
            if arr[i] not in vals:
                vals[arr[i]]=[]
            vals[arr[i]].append(i)
        def recurse(hbsb=set(),vsb=set()):
            s=deque()
            s.append((0,0))
            hbsb.add(0)
            while(s):
                pos,res=s.popleft()
                #print(s,pos,res)
                if pos==n-1:
                    return res
                if pos+1<n and pos+1 not in hbsb:
                    hbsb.add(pos+1)
                    s.append((pos+1,res+1))
                if pos-1>-1and pos-1 not in hbsb:
                    hbsb.add(pos-1)
                    s.append((pos-1,res+1))
                if arr[pos] not in vals:
                    continue
                for index in vals[arr[pos]]:
                    if index!=pos:
                        hbsb.add(index)
                        s.append((index,res+1))
                del vals[arr[pos]]
                
                #print(s,"\n")
        return recurse()

#attempt3: Similar version but still TLE
"""
from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[-1 for i in range(n)]
        dp[n-1]=0
        vals={}
        for i in range(n):
            if arr[i] not in vals:
                vals[arr[i]]=[]
            vals[arr[i]].append(i)
        def recurse(hbsb=set(),vsb=set()):
            s=deque()
            s.append((0,0))
            hbsb.add(0)
            while(s):
                pos,res=s.popleft()
                if pos==n-1:
                    return res
                if pos+1<n:
                    s.append((pos+1,res+1))
                if pos-1>-1:
                    s.append((pos-1,res+1))
                if arr[pos] in vsb:
                    continue
                vsb.add(arr[pos])
                for index in vals[arr[pos]]:
                    if index in hbsb:
                        continue
                    hbsb.add(index)
                    s.append((index,res+1))
                    
        return recurse()
"""

#attempt2: Used BFS but still TLE
"""
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[-1 for i in range(n)]
        dp[n-1]=0
        vals={}
        for i in range(n):
            if arr[i] not in vals:
                vals[arr[i]]=[]
            vals[arr[i]].append(i)
        def recurse(visited,hbsb=set()):
            while(True):
                newvisited={}
                for i in visited:
                    hbsb.add(i)
                    if i==n-1:
                        return visited[i]
                    if i-1>-1 and i-1 not in hbsb:
                        newvisited[i-1]=visited[i]+1
                    if i+1<n and i+1 not in hbsb:
                        newvisited[i+1]=visited[i]+1
                    for j in vals[arr[i]]:
                        if j not in hbsb:
                            newvisited[j]=visited[i]+1
                visited=newvisited.copy()
        return recurse({0:0})
"""

#attempt1: TLE USE BFS FOR PATH FINDING
"""
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[float('inf') for i in range(n)]
        dp[n-1]=0
        vals={}
        for i in range(n):
            if arr[i] not in vals:
                vals[arr[i]]=[]
            vals[arr[i]].append(i)
        def recurse(index,visited):
            if index>=n or index<0 or index in visited:
                return float('inf')
            if index==n-1:
                return 0
            ans=float('inf')
            ans=min(recurse(index+1,visited|{index}),recurse(index-1,visited|{index}))
            for i in vals[arr[index]]:
                if i!=index and i not in visited:
                    ans=min(ans,recurse(i,visited|{index}))
            return ans+1
        return recurse(0,set())
"""