#attempt2: TOOK HELP: COpied It is quite an easy problem.
#for an index n where n represents the number of elements currently
#to pick we can from choose n items to pick
#and out of the remaining 2*n-1 positions (because 2n is the total of pickups and
#deliveries) for the corresponding delivery
from math import factorial
class Solution:
    def countOrders(self, n: int) -> int:
        
        mod = 1000000007
        def findsol(n):
            if n==1:
                return 1
            return n*(2*n-1)*findsol(n-1)
        return findsol(n)%mod

#attempt1: WA My idea was that we can push elements onto the stack and
#at any point we can sell some number of items from the current stack and add
#a new element onto the stack for the next call
'''
from math import factorial
class Solution:
    def countOrders(self, n: int) -> int:
        
        mod = 1000000007
        """
        numbercurrent represents the picked items waiting to be delivered
        numbertotal represents the total number of items picked till now(delivered+undelivered)
        """
        @lru_cache(None)
        def recurse(numbercurrent,numbertotal):
            #print(numbercurrent,numbertotal)
            if numbertotal == n:
                return factorial(numbercurrent)%mod
            ans = 0
            for numberdelivered in range(numbercurrent+1):#we can deliver 'numberdelivered' items out of the current items in the stack
                    ans += recurse(numbercurrent-numberdelivered+1,numbertotal+1) + (factorial(numberdelivered))%mod
            return (ans*(n-numbertotal))%mod
        return recurse(0,0)
                
'''
