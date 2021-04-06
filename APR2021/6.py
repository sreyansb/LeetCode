#attempt1:
class Solution:
    def minOperations(self, n: int) -> int:
        aver=(2+(n-1)*2)//2
        ans=0
        for i in range(1,((2*n-1)//2)+1,2):
            ans+=abs(aver-i)
            #print(ans)
        return ans
        
        
