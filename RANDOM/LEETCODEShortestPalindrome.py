class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        maxlen=0
        for i in range(len(s),0,-1):
            if s[:i]==s[:i][::-1]:
                maxlen=i
                break
        return s[maxlen:][::-1]+s
        
            
        
        