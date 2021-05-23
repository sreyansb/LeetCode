#attempt3: TOOK HINT: AC 89% DP
class Solution:
    def numDecodings(self, S: str) -> int:
        n=len(S)
        dp={}
        if S[0]=='0':
            return 0
        def recurse(index):
            if index>=n-1:
                if (index==n-1 and S[index]!='0') or index>n-1:
                    return 1
                else:
                    return 0
            if S[index:] in dp:
                return dp[S[index:]]
            if S[index]=="0":
                return 0
            if S[index]=='1':
                if S[index+1]!='0':
                    dp[S[index:]]=recurse(index+1)+recurse(index+2)
                else:
                    dp[S[index:]]=recurse(index+2)
            elif S[index]=='2' and int(S[index+1])<7:
                if S[index+1]!='0':
                    dp[S[index:]]=recurse(index+1)+recurse(index+2)
                else:
                    dp[S[index:]]=recurse(index+2)
            else:
                dp[S[index:]]=recurse(index+1)
            return dp[S[index:]]
        return recurse(0)

#attempt2: Took Help -> not able to think
#it is like a fibonacci sequence
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        s=s.strip("0")
        if not(s) or s[0]=='0':
            return 0
        dp=[0]*(len(s)+1)#number of strings till length i
        dp[0]=1
        dp[1]=1
        for i in range(2,len(s)+1):
            if s[i-1]!='0':
                dp[i]+=dp[i-1]
            if s[i-2]=='1'  or (s[i-2]=='2' and s[i-1]<'7'):
                dp[i]+=dp[i-2]
        return dp[len(s)]
'''
#attempt1: WA twice
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        s=s.strip("0")
        if not(s):
            return 0
        dp={}
        def recurse(s,ans):
            if len(s)==0 or len(s)==1:
                ans[0]+=1
                return
            recurse(s[1:],ans)
            if s[:2]<"27" and s[0]!="0":
                recurse(s[2:],ans)
        ans=[0]
        recurse(s,ans)
        return ans[0]
        
"""
