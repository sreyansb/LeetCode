#attempt1: terrible timing
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans=0
        mod=1000000007
        n=len(arr)
        for i in range(n-2):
            li=[0 for i in range(301)]
            for j in range(i+1,n):
                ans+=li[target-arr[i]-arr[j]]
                ans%=mod
                li[arr[j]]+=1
                li[arr[j]]%=mod
        return ans%(mod)
