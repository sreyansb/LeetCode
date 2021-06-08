class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp={1:["()"]}
        
        for i in range(2,n+1):
            ans=set()
            for j in dp[i-1]:
                ans.add("()"+j)
                ans.add("("+j+")")
                ans.add(j+"()")
            for j in range(1,i//2+1):
                for k in dp[j]:
                    for l in dp[i-j]:
                        ans.add(k+l)
                        ans.add(l+k)
            dp[i]=list(ans)
        return dp[n]
            

                
            
