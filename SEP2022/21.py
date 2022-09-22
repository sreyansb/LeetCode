#attempt1:
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for word in s.split(" "):
            ans.append(word[::-1])
        return " ".join(ans)
    
            
        
