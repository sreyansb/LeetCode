#attempt1:
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        n=len(S)
        ans=[]
        power=0
        ans=0
        for i in range(n):
            if S[i]=="(":
                power+=1
            elif S[i-1]=="(":
                ans+=1<<(power-1)
                power-=1
            else:
                power-=1
        return ans
