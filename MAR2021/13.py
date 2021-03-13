#attempt2:Binary tree might have depth>1
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr=set(arr)
        count=0
        dp={}
        def countfactors(num):
            counter=1
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    if i in arr and num//i in arr:
                        j=2*dp[i]*dp[num//i]
                        if i==num//i:
                            j//=2#not divided by 4
                        counter+=j
            dp[num]=counter
            return dp[num]
        for i in sorted(arr):
            count+=countfactors(i)
        #print(dp)
        return count%((10**9)+7)
#attempt1:WA Assumed depth of tree==2
'''
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr=set(arr)
        count=len(arr)
        def countfactors(num):
            counter=0
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    if i in arr and num//i in arr:
                        counter+=2
                        if i==num//i:
                            counter-=1
            return counter
        for i in arr:
            count+=countfactors(i)
        return count%((10**9)+7)
            
            
'''
            
