#attempt2:
#TOOK HELP - wouldn't be able to think of it 
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
    
#Attempt1:Accepted:Very slow but great on memory
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i=1
        n=len(s)
        while(i<=n):
            k=s[:i]
            a=s.count(k)
            if a>1 and a*i==n:
                return True
            i+=1
        return False
            
            
        
