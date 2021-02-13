#attempt4: for path finding always use bfs compared to dfs
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        final=(rows-1,rows-1)
        infi=float('inf')
        i=0
        allowed=[(1,1),(1,0),(0,1),(-1,1),(1,-1),(-1,-1),(0,-1),(-1,0)]
        array=[(0,0)]
        visited={(0,0)}
        if grid[0][0]:
            return -1
        def valid(x1,x2):
            if x1>-1 and x1<rows and x2>-1 and x2<rows and not(grid[x1][x2]):
                return True
            return False
        while(array):
            #print(array)
            newarr=[]
            index=0
            while(index<len(array)):
                point=array[index]
                if point==final:
                    return i+1
                for j in allowed:
                    if valid(point[0]+j[0],point[1]+j[1]) and (point[0]+j[0],point[1]+j[1]) not in visited:
                        visited.add((point[0]+j[0],point[1]+j[1]))
                        newarr.append((point[0]+j[0],point[1]+j[1]))
                index+=1
            i+=1
            array=newarr
        return -1

#attempt 1,2,3 - all WA because of DFS usage
