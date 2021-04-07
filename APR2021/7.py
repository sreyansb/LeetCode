#attempt1
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        st=0
        nd=0
        vowels="aeiou"
        for i in range(len(s)//2):
            st+=1 if s[i] in vowels else 0
        for i in range(len(s)//2,len(s)):
            nd+=1 if s[i] in vowels else 0
        return st==nd
            
