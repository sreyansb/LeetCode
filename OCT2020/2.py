#ATTEMPT2 : 15% and 6%
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=set()
        def dp(visited,val):
            if val==0:
                ans.add(tuple(sorted(visited)))
            for i in candidates:
                if val-i>=0:
                    dp(visited+[i],val-i)
        for i in candidates:
            if i<=target:
                dp([i],target-i)
        return list(ans)

#ATTEMPT1: 11% and 11%
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=set()
        def dp(visited,val):
            if val<0:
                return 
            if val==0:
                ans.add(tuple(sorted(visited)))
            for i in candidates:
                if val-i>=0:
                    dp(visited+[i],val-i)
        for i in candidates:
            dp([i],target-i)
        return list(ans)
"""
