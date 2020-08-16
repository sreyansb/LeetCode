class Solution:
    def maxProfit(self, a: List[int]) -> int:
        n=len(a)
        maxi=0
        for i in range(1,n):
            if a[i]>a[i-1]:
                maxi+=a[i]-a[i-1]
        return maxi
    
obj=Solution()
print(obj.maxProfit([7,6,4,3,1]))

