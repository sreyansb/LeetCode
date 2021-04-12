#attempt2: TOOK HELP

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        if k==1:
            return list(range(1,n+1))
        c=n-k
        ans=list(range(1,c+1))
        ans.append(n)
        leng=len(ans)
        while(leng<n):
            ans.append(ans[-2]+1)
            leng+=1
            if leng<n:
                leng+=1
                ans.append(ans[-2]-1)
        return ans
            
            
            
            
