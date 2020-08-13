class Solution:
    def isNumber(self, s: str) -> bool:
        ans=True
        s=s.strip()
        print(s)
        try:
            s=float(s)
        except:
            ans=False
        return ans
            
        
        
