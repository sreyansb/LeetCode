#attempt1: 75% and 99%
from bisect import bisect_right
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        index=0
        n=len(A)
        ans=[]
        while(A):
            pos=bisect_right(A,B[index])
            ele=-1
            if pos==n:
                ele=A[0]
                ans.append(ele)
                del A[0]
            else:
                ele=A[pos]
                ans.append(ele)
                del A[pos]              
            n-=1
            index+=1
        return ans
            
        
