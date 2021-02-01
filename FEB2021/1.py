#attempt1:
class Solution:
    def hammingWeight(self, n: int) -> int:
        number=0
        while(n):
            number+=n&1
            n>>=1
        return number

#attempt2:
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while(n):
            count+=1
            n&=(n-1)
        return count
        
'''
        
