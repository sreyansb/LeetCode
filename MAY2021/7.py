#attempt1: I think Advanced Algo had a similar problem
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[-1 for i in range(m)] for j in range(n)]
        def find(i,j):
            if i==-1 or j==-1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i]==word2[j]:
                dp[i][j]=1+find(i-1,j-1)
            else:
                dp[i][j]=max(find(i-1,j),find(i,j-1))
            return dp[i][j]
        return m+n-2*find(n-1,m-1)
        
