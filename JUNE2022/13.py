#attempt1:
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        ans = float('inf')
        
        @lru_cache(None)
        def findans(row,col):
            if row >= n:
                return 0
            return triangle[row][col] + min(findans(row+1,col),findans(row+1,col+1))
        
        for col in range(len(triangle[0])):
            ans = min(ans,triangle[0][col]+findans(1,col),triangle[0][col]+findans(1,col+1))
        
        return ans
            
        
