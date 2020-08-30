#attempt 4: had to take help
#used union-find structures
import collections
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        
        n=len(A)
        maxi=max(A)
        factors=[i for i in range(maxi+1)]
        
        def find(a):
            while(factors[a]!=a):
                factors[a]=factors[factors[a]]
                a=factors[a]
            return a
            
        def union(a,b):
            if factors[a]==factors[b]:
                return
            parenta=find(a)
            parentb=find(b)
            factors[parenta]=parentb
            
        for x in A:
            for i in range(2,int(x**0.5)+1):
                if x%i==0:
                    union(x,i)
                    union(x,x//i)
        count={}
        for x in A:
            a=find(x)
            if a not in count:
                count[a]=0
            count[a]+=1
        return max(count.values())
"""
#attempt 3: passed 71/100:TLE
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        
        def calculate(spf):
            maxn=10**5+2
            for i in range(4,maxn,2):
                spf[i]=2
            for i in range(3,317,2):
                for j in range(i*i,maxn,i):
                    spf[j]=min(spf[j],i)
            return spf
        
        n=len(A)
        spf=[i for i in range(10**5+2)]
        calculate(spf)
        factors=[set() for _ in range(n)]
        
        def getfactors(i):
            S=set()
            while(i>1):
                S.add(spf[i])
                i//=spf[i]
            return S
                
        for i in range(n):
            factors[i]=getfactors(A[i])
        
        grid=[[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                if factors[i]&factors[j]:
                        grid[i].append(j)
                        grid[j].append(i)
        
        def dfs(vertex,visited):
            if vertex in visited:
                return
            visited.add(vertex)
            for i in grid[vertex]:
                dfs(i,visited)
            
        maxi=1
        allvisited=set()
        for i in range(n):
            if i not in allvisited:
                visited=set()
                dfs(i,visited)
                maxi=max(maxi,len(visited))
                allvisited=allvisited|visited
        return maxi
"""

"""
#attempt 2-> passed 74/100:TLE
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        n=len(A)
        factors=[set() for _ in range(n)]
        
        def getfactors(i):
            S={i}
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    S.add(j)
                    S.add(i//j)
            return S
        
        for i in range(n):
            factors[i]=getfactors(A[i])
        
        grid=[[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                if factors[i]&factors[j]:
                        grid[i].append(j)
                        grid[j].append(i)
        
        def dfs(vertex,visited):
            if vertex in visited:
                return
            visited.add(vertex)
            for i in grid[vertex]:
                dfs(i,visited)
            
        maxi=1
        allvisited=set()
        for i in range(n):
            if i not in allvisited:
                visited=set()
                dfs(i,visited)
                maxi=max(maxi,len(visited))
                allvisited=allvisited|visited
        return maxi
"""

"""
#Attempt 1 -> passed 71/100 : TLE
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        n=len(A)
        factors=[set() for _ in range(n)]
        
        def getfactors(i):
            S={i}
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    S.add(j)
                    S.add(i//j)
            return S
        
        for i in range(n):
            factors[i]=getfactors(A[i])
        
        grid=[[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if factors[i]&factors[j]:
                        grid[i].append(j)
                        grid[j].append(i)
        
        def dfs(vertex,visited):
            if vertex in visited:
                return
            visited.add(vertex)
            for i in grid[vertex]:
                dfs(i,visited)
            
        maxi=1
        allvisited=set()
        for i in range(n):
            if i not in allvisited:
                visited=set()
                dfs(i,visited)
                maxi=max(maxi,len(visited))
                allvisited=allvisited|visited
        return maxi
"""
