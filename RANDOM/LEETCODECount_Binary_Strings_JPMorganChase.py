#attempt1:
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n=len(s)
        ans=0
        i=0
        while(i<n):
            j=i+1
            while(j<n and s[j]==s[i]):
                j+=1
            k=j+1
            while(k<n and s[k]==s[j]):
                k+=1
            if j==n:
                ans+=0
            else:
                ans+=min(j-i,k-j)
                #print(i,j,k,ans)
            i=j
        return ans
            
            
        
