#attempt3: This was an attempt I had already made before. Better to revise
#and look at problems properly
class Solution:
    def countBinarySubstrings(self, a: str) -> int:
        n=len(a)
        if n<=1:
            return 0
        right=0
        left=0
        count=0
        while(right<n):
            j=right+1
            while(j<n and a[j]==a[right]):
                j+=1
            if j==n:
                break
            k=j+1
            while(k<n and a[j]==a[k]):
                k+=1
            count+=min(j-right,k-j)   
            right=j
            
        return count

#attempt2:TOOK HELP
'''
class Solution:
    def countBinarySubstrings(self, a: str) -> int:
        n=len(a)
        if n<=1:
            return 0
        tot=0
        cur=1
        prev=0
        for i in range(1,n):
            if a[i]==a[i-1]:
                cur+=1
            else:
                tot+=min(cur,prev)
                prev,cur=cur,1
                        
        return tot+min(cur,prev)
        
'''

#attempt1:HAD FORGOTTEN STUFF COMPLETELY WA
'''
class Solution:
    def countBinarySubstrings(self, a: str) -> int:
        n=len(a)
        if n<=1:
            return 0
        right=1
        left=0
        count=0
        while(right<n):
            #print(left,right)
            if int(a[right])^int(a[left])==1:
                lc=left
                rc=right
                leng=0
                while(lc>=0 and rc<n and int(a[lc])^int(a[rc])==1):
                    leng+=1
                    lc-=1
                    rc+=1
                count+=leng
                right=rc
                left=rc-1
            else:
                right+=1
                left+=1
            
        return count
'''
