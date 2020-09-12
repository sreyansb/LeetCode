#attempt 8 -95.70% -> random changes not actual optimization
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dp=[[0 for i in range(n+1)] for j in range(k+1)]
        
        for i in range(1,n+1):
            dp[1][i]=[[i]]
            
        def find(k,n,visited):
            if k<=0 or n<=0:
                return []
            
            if dp[k][n]!=0:
                return dp[k][n]
            
            dp[k][n]=[]
            for i in range(1,10):
                if i not in visited:
                    j=find(k-1,n-i,visited|{i})
                    for l in j:
                        z=[i]+l
                        m=sorted(z)
                        if sum(z)==n and len(set(z))==k and max(z)<10 and m not in dp[k][n]:
                            dp[k][n].append(m)
            return dp[k][n]
        
        find(k,n,set())
        sol1=[]
        for i in dp[k][n]:
            sol1.append(list(i))
        return sol1
        

#attempt 7: Accepted DP ->faster 68% ->made some small reduntant changes
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dp=[[0 for i in range(n+1)] for j in range(k+1)]
        
        for i in range(1,n+1):
            dp[1][i]=[[i]]
            
        def find(k,n,visited):
            if k<=0 or n<=0:
                return []
            
            if dp[k][n]!=0:
                return dp[k][n]
            
            dp[k][n]=[]
            for i in range(1,10):
                if i not in visited:
                    j=find(k-1,n-i,visited|{i})
                    if j:
                        for l in j:
                            z=[i]+l
                            m=sorted(z)
                            if sum(z)==n and len(set(z))==k and max(z)<10 and m not in dp[k][n]:
                                dp[k][n].append(m)
            return dp[k][n]
        
        find(k,n,set())
        sol1=[]
        for i in dp[k][n]:
            sol1.append(list(i))
        return sol1
"""        


#attempt 6: Accepted-DP approach, less space, faster 30%
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dp=[[0 for i in range(n+1)] for j in range(k+1)]
        
        for i in range(1,n+1):
            dp[1][i]=[[i]]
            
        def find(k,n,visited):
            if k<=0 or n<=0:
                return []
            
            if dp[k][n]!=0:
                return dp[k][n]
            
            dp[k][n]=[]
            for i in range(1,10):
                if i not in visited:
                    j=find(k-1,n-i,visited|{i})
                    if j:
                        for l in j:
                            z=[i]+l
                            if sum(z)==n and len(set(z))==k and max(z)<10 and sorted(z) not in dp[k][n]:
                                dp[k][n].append(sorted(z))
            return dp[k][n]
        
        find(k,n,set())
        sol1=[]
        for i in dp[k][n]:
            sol1.append(list(i))
        return sol1
"""

#attempt5: Accepted DP took a lot of time 128ms
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dp=[[0 for i in range(n+1)] for j in range(k+1)]
        
        for i in range(1,n+1):
            dp[1][i]=[[i]]
            
        def find(k,n,ans,visited):
            if k<=0 or n<=0:
                return []
            
            if dp[k][n]!=0:
                if k==1 and n>0 and n<10 and n not in visited:
                    ans.add(tuple(sorted(visited|{n})))
                return dp[k][n]
            
            dp[k][n]=[]
            for i in range(1,10):
                if i not in visited:
                    j=find(k-1,n-i,ans,visited|{i})
                    if j:
                        for l in j:
                            if sum(l+[i])==n and len(set([i]+l))==k and max([i]+l)<10:
                                dp[k][n].append(sorted([i]+l))
            return dp[k][n]
            
        ans=set()
        sol=find(k,n,ans,set())
        sol=set()
        for i in dp[k][n]:
            sol.add(tuple(i))
        sol1=[]
        for i in sol:
            sol1.append(list(i))
        return sol1
"""        

#attempt4: Accepted very slow: 1224ms but 95% space.
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def find(k,n,ans,visited):
            if k<=0 or n<=0:
                return
            if k==1 and n>0 and n<10 and n not in visited:
                ans.add(tuple(sorted(visited|{n})))
            for i in range(1,10):
                if i not in visited:
                    find(k-1,n-i,ans,visited|{i})
            
        ans=set()
        sol=find(k,n,ans,set())
        sol=[]
        for i in ans:
            if sum(i)==n:
                sol.append(list(i))
        return sol
"""        

#attempt3: TLE -> 17/18 -> in the for loop made a change if an element was in
#visited or not
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def find(k,n,ans,visited):
            if k<=0 or n<=0:
                return
            if k==1 and n>0 and n<10 and n not in visited:
                ans.add(tuple(sorted(visited|{n})))
            for i in range(1,10):
                find(k-1,n-i,ans,visited|{i})
            
        ans=set()
        sol=find(k,n,ans,set())
        sol=[]
        for i in ans:
            if sum(i)==n:
                sol.append(list(i))
        return sol
"""

#attempt2: WA gave an extra same list
#because tuples are not like sets and hence they are not compared by elements
#they have but element by element.
#hence sorted each tuple before adding to answer
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def find(k,n,ans,visited):
            if k<=0 or n<=0:
                return
            if k==1 and n>0 and n<10 and n not in visited:
                ans.add(tuple(visited|{n}))
            for i in range(1,10):
                find(k-1,n-i,ans,visited|{i})
            
        ans=set()
        sol=find(k,n,ans,set())
        sol=[]
        for i in ans:
            if sum(i)==n:
                sol.append(list(i))
        return sol
"""

#attempt 1: WA was giving answers as 13+5 for 18.
#changed conditions to append a solution to visited
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def find(k,n,ans,visited):
            if k<=0 or n<=0:
                return
            if k==1 and n and n not in visited:
                ans.add(tuple(visited|{n}))
            for i in range(1,n+1):
                find(k-1,n-i,ans,visited|{i})
            
        ans=set()
        sol=find(k,n,ans,set())
        sol=[]
        for i in ans:
            if sum(i)==n:
                sol.append(list(i))
        return sol
        
"""
