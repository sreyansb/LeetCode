class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        if not(s):
            return True
        k=""
        for i in s:
            if (i>='a' and i<='z') or (i>='0' and i<='9'):
                k+=i
        n=len(k)
        for i in range(n//2+n%2):
            if k[i]!=k[n-1-i]:
                return False
        return True
        
