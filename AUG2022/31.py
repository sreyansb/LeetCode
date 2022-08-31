#attempt1:
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowl = len(heights)
        coll = len(heights[0])
        
        def dfs(row,col,allvisited):
            allvisited.add((row,col))
            for nextr,nextc in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                if not(0<=nextr<rowl and 0<=nextc<coll) or heights[nextr][nextc] < heights[row][col] or (nextr,nextc) in allvisited:
                    continue
                dfs(nextr,nextc,allvisited)
        
        pacificOcean = set()
        atlanticOcean = set()
        
        for col in range(coll):
            dfs(0,col,pacificOcean)
            dfs(rowl-1,col,atlanticOcean)
        for row in range(rowl):
            dfs(row,0,pacificOcean)
            dfs(row,coll-1,atlanticOcean)
        return list(pacificOcean & atlanticOcean)
                    
            
