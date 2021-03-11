#attempt2: 75%
from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dpt=[inf for i in range(amount+1)]
        dpt[0]=0
        for i in coins:
            for producible_amts in range(i,amount+1):
                dpt[producible_amts]=min(dpt[producible_amts],1+dpt[producible_amts-i])
        if dpt[-1]==inf:
            return -1
        return dpt[-1]

#attempt1:30%
'''
from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dpt={}
        def dp(amount):
            if amount<0:
                return inf
            if amount==0:
                return 0
            if amount in dpt:
                return dpt[amount]
            curamt=inf
            for i in coins:
                curamt=min(curamt,1+dp(amount-i))
            dpt[amount]=curamt
            return curamt
        k=dp(amount)
        if k==inf:
            return -1
        return k
'''
