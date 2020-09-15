#attempt2:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        curlength=0
        for i in range(len(s)):
            if s[i]!=" " :
                if i>0 and s[i-1]==" ":
                    curlength=0               
                curlength+=1
        return curlength

#attempt 1:
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not(s):
            return 0
        s=s.strip(" ")
        k=s.split(" ")
        return len(k[-1])
"""      
