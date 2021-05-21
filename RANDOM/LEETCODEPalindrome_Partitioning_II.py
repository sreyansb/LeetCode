#attempt2: TOOK HELP
class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        @lru_cache(None)
        def recurse(i):
            if i==n:
                return 0
            ans=float('inf')
            for j in range(i+1,n+1):
                k=s[i:j]
                if k==k[::-1]:
                    ans=min(ans,1+recurse(j))
            return ans
        return recurse(0)-1
                    
                
        
# attempt1: TLE 24/33 tried to make use of the code from palindrome partitioning
#but here constraints are len(s)<=2000 -> TLE
'''
class Solution:
    def minCut(self, s: str) -> int:
        ans=[]
        n=len(s)
        dp=[[False for i in range(n)]for i in range(n)]
        def recurse(left,curlist):
            if left>=n:
                ans.append(len(curlist))
            for i in range(left,n):
                if s[i]==s[left] and (i-left+1<3 or dp[left+1][i-1]):
                    dp[left][i]=True
                    recurse(i+1,curlist+[s[left:i+1]])
        recurse(0,[])
        #print(ans)
        return min(ans)-1
        
'''