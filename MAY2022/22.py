#attempt1:
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = [0]
        
        def dp(start,end):
            while(start>=0 and end<n):
                if s[start] == s[end]:
                    start -= 1
                    end += 1
                    ans[0] += 1
                else:
                    break
        
        for i in range(n):
            dp(i,i)
            dp(i,i+1)
        return ans[0]
            
                        
