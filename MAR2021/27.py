#attempt1:
class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        if not n:
            return 0
        
        ans=[0]
        def checkifpalindrome(start,end):
            while(start>-1 and end<n and s[start]==s[end]):
                start-=1
                end+=1
                ans[0]+=1
        for i in range(n):
            checkifpalindrome(i,i)
            checkifpalindrome(i,i+1)
        return ans[0]
        
