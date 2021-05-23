#accepted attempt: TOOK HELP JUST COPIED
class Solution:
    def CreateConnections(self, A, N):
        Connections = [[""] * N for _ in range(N)]
        for i, j in permutations(range(N), 2):
            Connections[i][j] = A[j]
            for k in range(min(len(A[i]), len(A[j]))):
                if A[i][-k:] == A[j][:k]:
                    Connections[i][j] = A[j][k:]
        return Connections

    def shortestSuperstring(self, A):
        N = len(A)
        Connections = self.CreateConnections(A, N)
        dp = [[(float("inf"), "")] * N for _ in range(1<<N)]
        for i in range(N): dp[1<<i][i] = (len(A[i]), A[i])
            
        for mask in range(1<<N):
            n_z_bits = [j for j in range(N) if mask&(1<<j)]
            
            for j, k in permutations(n_z_bits, 2):
                cand = dp[mask ^ (1<<j)][k][1] + Connections[k][j]
                dp[mask][j] = min(dp[mask][j], (len(cand), cand))

        return min(dp[-1])[1]   

#attempt4: TLE 72/83 DFS with pruning and DP and bit masking
'''
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n=len(words)
        dp=[["" for i in range(n)]for j in range(n)]#dp[i][j] stores length and concatenated strings
        
        for i in range(n):
            for j in range(n):
                if i==j:
                    dp[i][j]=(float('inf'),words[i])
                else:
                    o,m=len(words[i]),len(words[j])
                    start=max(0,o-m)
                    maxi=0
                    for z in range(start,o):
                        k=0
                        while(k<m and z+k<o and words[i][z+k]==words[j][k]):
                                k+=1
                        if z+k==o:
                            maxi=k
                            break
                    dp[i][j]=(m-maxi,j,words[j][maxi:])
        
        mini=[float('inf')]
        finans=[""]
        minvalue=[float('inf')]
        def recurse(visited,index,curstr):
            k1=len(curstr)
            
            if visited==(1<<n)-1:
                mini[0]=min(mini[0],k1)
                if mini[0]==k1:
                    finans[0]=curstr
                    minvalue[0]=min(minvalue[0],k1)
                return
            
            if k1>=minvalue[0]:
                return
            
            for i in range(n):
                    if visited&(1<<i)==0 and k1+dp[index][i][0]<minvalue[0]:
                        recurse(visited|(1<<i),i,curstr+dp[index][i][-1])
        for i in range(n):
            recurse(1<<i,i,words[i])
        #print(mini[0])
        return finans[0]
'''

#attempt3:TLE 72/83 DFS with pruning and DP
'''
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n=len(words)
        dp=[["" for i in range(n)]for j in range(n)]#dp[i][j] stores length and concatenated strings
        for i in range(n):
            for j in range(n):
                if i==j:
                    dp[i][j]=(float('inf'),words[i])
                else:
                    o,m=len(words[i]),len(words[j])
                    start=max(0,o-m)
                    maxi=0
                    for z in range(start,o):
                        k=0
                        while(k<m and z+k<o and words[i][z+k]==words[j][k]):
                                k+=1
                        if z+k==o:
                            maxi=k
                            break
                    dp[i][j]=(n+m-maxi,j,words[j][maxi:])
        mini=[float('inf')]
        finans=[""]
        minvalue=[float('inf')]
        def recurse(visited,index,curstr):
            k1=len(curstr)
            
            if len(visited)==n:
                mini[0]=min(mini[0],k1)
                if mini[0]==k1:
                    finans[0]=curstr
                    minvalue[0]=min(minvalue[0],k1)
                return
            
            if k1>=minvalue[0]:
                return
            
            for i in range(n):
                    if i not in visited:
                        recurse(visited|{i},i,curstr+dp[index][i][-1])
        for i in range(n):
            recurse({i},i,words[i])
        #print(mini[0])
        return finans[0]
'''

#attempt2:TLE 65/83 DFS with pruning
'''
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n=len(words)
        mini=[float('inf')]
        finans=[""]
        minvalue=[float('inf')]
        def recurse(visited,curstr):
            k1=len(curstr)
            if len(visited)==n:
                
                mini[0]=min(mini[0],k1)
                if mini[0]==k1:
                    finans[0]=curstr
                    minvalue[0]=min(minvalue[0],k1)
                return
            if k1>=minvalue[0]:
                return
            for i in range(n):
                    if i not in visited:
                        maxi=0
                        #find longest suffix of curstr which is a prefix of words[i]
                        start=max(0,k1-len(words[i]))
                        for j in range(start,k1):
                            k=0
                            while(j+k<k1 and k<len(words[i]) and curstr[j+k]==words[i][k]):
                                k+=1
                            if j+k==k1:
                                maxi=max(maxi,k)
                        recurse(visited+[i],curstr+words[i][maxi:])
        recurse([],"")
        #print(mini[0])
        return finans[0]
'''

#attempt1:TLE 52/83 O(n!) time EXPECTED A TLE but coding a brute force also took time, I wasn't efficient.
#Committed many mistakes
"""
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n=len(words)
        mini=[float('inf')]
        finans=[""]
        def recurse(visited,curstr):
            if len(visited)==n:
                mini[0]=min(mini[0],len(curstr))
                if mini[0]==len(curstr):
                    finans[0]=curstr
            else:
                for i in range(n):
                    if i not in visited:
                        maxi=0
                        #find longest suffix of curstr which is a prefix of words[i]
                        start=max(0,len(curstr)-len(words[i]))
                        for j in range(start,len(curstr)):
                            k=0
                            while(j+k<len(curstr) and k<len(words[i]) and curstr[j+k]==words[i][k]):
                                k+=1
                            if j+k==len(curstr):
                                maxi=max(maxi,k)
                        '''
                        if i==4 and curstr=="catgctaagttca":
                            print(visited,maxi,curstr+words[i][maxi:])
                        
                        if visited==[0] and i==4:
                            print("here",maxi,curstr+words[i][maxi:])
                        '''
                        recurse(visited+[i],curstr+words[i][maxi:])
        recurse([],"")
        #print(mini[0])
        return finans[0]
"""

'''
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n1=len(words)
        dp=[["" for i in range(n1)]for j in range(n1)]#dp[i][j] stores length and concatenated strings
        for i in range(n1):
            for j in range(n1):
                if i==j:
                    dp[i][j]=(float('inf'),words[i])
                else:
                    n,m=len(words[i]),len(words[j])
                    start=max(0,n-m)
                    maxi=0
                    for z in range(start,n):
                        k=0
                        while(k<m and z+k<n and words[i][z+k]==words[j][k]):
                                k+=1
                        if z+k==n:
                            maxi=k
                            break
                    dp[i][j]=(n+m-maxi,j,words[j][maxi:])
        dp=[sorted(i,key=lambda x:x[0]) for i in dp]
        minie=[float('inf')]
        finans=[""]
        def recurse(index,visited,curstr):
            if len(visited)==n:
                k=len(curstr)
                minie[0]=min(minie[0],k)
                if minie[0]==k:
                    finans[0]=curstr
                return
            for 
'''