#attempt2: 11%
from bisect import bisect_left
class Solution:
    def numSquares(self, n: int) -> int:
        
        def get_perfect_squares(n):
            squares = []
            i = 1
            while(i*i <= n):
                squares.append(i*i)
                i += 1
            return squares
        
        squares = get_perfect_squares(n)
        setsquares = set(squares)
        
        @lru_cache(None)
        def get_min(n):
            if n in setsquares:
                return 1
            pos = bisect_left(squares,n)
            ans = float('inf')
            for ele in squares[:pos]:
                ans = min(ans,1+get_min(n-ele))
            return ans
        return get_min(n)
            
#attempt1: 5% I think should've been faster than attempt2
'''
from bisect import bisect_left
class Solution:
    def numSquares(self, n: int) -> int:
        
        def get_perfect_squares(n):
            squares = []
            i = 1
            while(i*i <= n):
                squares.append(i*i)
                i += 1
            return squares
        
        squares = get_perfect_squares(n)
        setsquares = set(squares)
        
        @lru_cache(None)
        def get_min(n):
            if n in setsquares:
                return 1
            pos = bisect_left(squares,n)
            ans = float('inf')
            for ele in squares[:pos][::-1]:
                ans = min(ans,1+get_min(n-ele))
            return ans
        return get_min(n)
'''