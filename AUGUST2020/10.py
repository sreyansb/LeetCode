class Solution:
    def titleToNumber(self, s: str) -> int:
        colno=0
        b=1
        for i in s[::-1]:
            colno+=(ord(i)-64)*b
            b*=26
        return colno
            
            
        
