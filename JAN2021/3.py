#attempt2: AC took help from leetcode discuss
#it is a problem of DFS and backtracking, easy it was.
class Solution:
    def countArrangement(self, n: int) -> int:
        visited=[0]*(n+2)
        ans=[0]
        def dfs(index):
            if index==n+1:
                ans[0]+=1
                #print(ans)
            for i in range(1,n+1):#for index i put all possible values and
                #do stuff for index+1
                if visited[i]==0 and (i%index==0 or index%i==0):
                    visited[i]=1
                    dfs(index+1)
                    visited[i]=0
        dfs(1)
        return ans[0]

#attempt1: WA 1-6 correct wrong idea but
'''
class Solution:
    def countArrangement(self, n: int) -> int:
        ans=1
        i=1
        while(n//i>0):
            ans*=n//i
            i+=1
        return ans
            
        
'''
