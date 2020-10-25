#attempt2: AC -> had to use a squares array which has all squares below
#int(n**0.5)**2
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp={}
        squares=[i*i for i in range(1,int(n**0.5)+1)]
        def calc(c):
            if c==0:
                return False
            if c**0.5==int(c**0.5):
                return True
            if c in dp:
                return dp[c]
            ans=False
            for j in squares:
                if j>c:
                    ans=False
                    break
                ans=(calc(c-j)^calc(j))#calc(j) is always True=>not(calc(c-j))
                if ans:
                    break
            dp[c]=ans
            return dp[c]
        return calc(n)

#attempt1: WA 46/72
"""
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp={}
        def calc(c):
            if c==0:
                return False
            if c**0.5==int(c**0.5):
                return True
            if c in dp:
                return dp[c]
            dp[c]=(calc(c-int(c**0.5)**2)^calc(int(c**0.5)**2)) or (True ^ calc(c-1))
            return dp[c]
        return calc(n)
"""           
        
