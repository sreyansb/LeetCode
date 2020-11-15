class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a=sorted(nums)
        ans=[a.copy()]
        flag=1
        n=len(a)-1
        while(flag):
            #print(a)
            if a==sorted(a,reverse=True):
                break
            i,j=n,n
            while(i>0):
                if a[i]>a[i-1]:
                    break
                i-=1
            while(j>=i):
                if a[j]>a[i-1]:
                    break
                j-=1
            a[j],a[i-1]=a[i-1],a[j]
            a[i:]=a[i:][::-1]
            ans.append(a.copy())
        return ans
                    
        
        
