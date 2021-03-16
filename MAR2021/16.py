#attempt2:remove function calls
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        k=-float('inf')
        dpt=[[k for i in range(2)] for j in range(n)]#dpt[index][0]-buy->you have a stock on that day
        for index in range(n):
            if index==0:
                dpt[index][0]=-prices[index]
                dpt[index][1]=0
            else:
                dpt[index][0]=max(dpt[index-1][1]-prices[index],dpt[index-1][0])
                dpt[index][1]=max(dpt[index][0]+prices[index]-fee,dpt[index-1][1])
        #print(dpt)
        return max(0,dpt[n-1][1])

#attempt1: Thank God! I remembered!
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        k=-float('inf')
        dpt=[[k for i in range(2)] for j in range(n)]
        #dpt[index][0]-buy->you have a stock on that day
        #dpt[index][1]-> no stock
        def dp(index=0):
            if index==n:
                return
            if index==0:
                dpt[index][0]=-prices[index]
                dpt[index][1]=0
            else:
                dpt[index][0]=max(dpt[index-1][1]-prices[index],dpt[index-1][0])
                dpt[index][1]=max(dpt[index][0]+prices[index]-fee,dpt[index-1][1])
            dp(index+1)
        dp()
        #print(dpt)
        return max(0,dpt[n-1][1])
'''
