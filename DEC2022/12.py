#attempt1:
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def findAns(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return findAns(n-1) + findAns(n-2)
        return findAns(n)
