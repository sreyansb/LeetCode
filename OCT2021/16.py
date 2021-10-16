#attempt3: 1442ms : an old submission of 72ms!
'''
from math import inf
class Solution:
    def maxProfit(self, a: List[int]) -> int:
        if not(a):
            return 0
        fb=-inf#maximise first buy
        fs=-inf#maximise first sell
        sb=-inf#maximise second buy
        ss=-inf#maximise second sell
        for i in a:
            fb=max(fb,-i)
            fs=max(fs,fb+i)
            sb=max(sb,fs-i)
            ss=max(ss,sb+i)
        return ss
'''

#attempt2: 1616ms
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        b1,b2,s1,s2 = -float('inf'),-float('inf'),0,0
        b1 = -prices[0]
        for i in range(1,n):
            b1 = max(b1,-prices[i])
            s1 = max(s1,b1+prices[i])
            b2 = max(b2,s1-prices[i])
            s2 = max(s2,b2+prices[i])
        return max(s1,s2)
''' 

#attempt1: 1315ms

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = [0]*n
        buy2 = [-float('inf')]*n
        sell1 = [0]*n
        sell2 = [0]*n
        buy1[0] = -prices[0]
        for i in range(1,n):
            buy1[i] = max(buy1[i-1],-prices[i])
            sell1[i] = max(sell1[i-1],buy1[i]+prices[i])
            buy2[i] = max(buy2[i-1],sell1[i]-prices[i])
            sell2[i] = max(sell2[i-1],buy2[i]+prices[i])
        return max(sell1[-1],sell2[-1])
