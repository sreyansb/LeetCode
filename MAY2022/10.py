#attempt1:
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = set()
        def dp(currentk,currentsum,visited):
            if currentk == 0 and currentsum == 0:
                ans.add(tuple(sorted(visited)))
                return
            elif currentsum <= 0 or currentk == 0:
                return
            for i in range(1,min(9,currentsum)+1):
                if i not in visited:
                    dp(currentk-1,currentsum-i,visited+[i])
            return
        dp(k,n,[])
        return ans
                    
                    
            
        
