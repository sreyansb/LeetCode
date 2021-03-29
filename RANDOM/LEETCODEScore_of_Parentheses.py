#ALL attempts TOOK HELP

#attempt1: Push for every ( a 0 and pop when you see ) and add to last element
#of stack. Always 1 element stays
'''
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        n=len(S)
        ans=[0]
        for i in range(n):
            if S[i]=='(':
                ans.append(0)
            else:
                v=ans.pop()
                ans[-1]+=max(1,2*v)
        return ans[-1]
'''

#attempt2:
'''
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        n=len(S)
        power,ans=0,0
        for i in range(n):
            if S[i]=='(':
                power+=1
            else:
                if S[i-1]=='(':
                    ans+=1<<(power-1)
                    power-=1
                else:
                    power-=1
        return ans
'''
