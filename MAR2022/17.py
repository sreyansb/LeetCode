#attempt1:
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        i = 0
        openpar = 0
        while(i<len(s)):
            char = s[i]
            if char == "(":
                openpar += 1
            elif char == ")":
                openpar -= 1
                if s[i-1] == "(":
                    ans += 1<<openpar
            i += 1
        return ans
                    
                    
                    
        
        
