#attempt1: Generating Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp={1:["()"]}
        if n==1:
            return dp[1]
        for i in range(2,n+1):
            dp[i]=set()
            for j in dp[i-1]:
                dp[i].add("()"+j)
                dp[i].add(j+"()")
                dp[i].add("("+j+")")
            for j in range(1,i//2+1):
                for l in dp[j]:
                    for k in dp[i-j]:
                        dp[i].add(l+k)
                        dp[i].add(k+l)
        return list(dp[n])
            
        