'''
#Had many attempts: REGEX needs to be thought out ptoperly
#POINTS
#before an e/E there has to be a digit
#attempt8:
import re
class Solution:
    def isNumber(self, s: str) -> bool:       
        pattern=r"^([+-]?([0-9]+|[0-9]*\.[0-9]+|[0-9]+\.[0-9]*))([Ee][+-]?[0-9]+)?$"
        return bool(re.match(pattern,s))

#attempt5: WHEN making use of float(string), need to understand that inf/infinity
#can also be converted into a float
import re
class Solution:
    def isNumber(self, s: str) -> bool:
        if "inf" in s or "Infinity" in s:
            return False
        try:
            k=float(s)
            return True
        except:
            return False    



'''
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
            
        
        
