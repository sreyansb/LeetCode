class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:                
        def helper(n,v,curlevel,s):
            if n==0:
                curlevel.add(s)
            if n<0 or v<0 or v>9:
                return
            helper(n-1,(v-K),curlevel,s*10+v)
            helper(n-1,(v+K),curlevel,s*10+v)
        
        ans=set()
        index=1
        if N==1:
            index=0
        for i in range(index,10):
            curlevel=set()
            helper(N-1,(i-K),curlevel,i)
            helper(N-1,(K+i),curlevel,i)
            ans|=curlevel
        return(list(ans))

obj=Solution()
print(obj.numsSameConsecDiff(3,1))
