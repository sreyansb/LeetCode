#attempt1:
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not(amount):
            return 0
        @lru_cache(None)
        def coin_change(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            ans = float('inf')
            for coin in coins:
                ans = min(ans,1+coin_change(amount-coin))
            return ans
        ans = coin_change(amount)
        return ans if ans != float('inf') else -1
                
                
            
        
