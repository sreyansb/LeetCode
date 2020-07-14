class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=1
        n=len(digits)
        carry=1
        while(x<=n and digits[-x]==9):
            digits[-x]=0
            carry=1
            x+=1
        if x==n+1:
            digits=[1]+digits
        else:
            digits[-x]+=carry
        return digits
        
            
            
        
