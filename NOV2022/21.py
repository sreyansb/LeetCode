#aattempt1:
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([[entrance[0],entrance[1],0]])
        m,n = len(maze),len(maze[0])
        visited = {(entrance[0],entrance[1])}
        while(queue):
            currentRow,currentCol, steps = queue.popleft()
            if steps != 0 and (currentRow==0 or currentCol==0 or currentCol==n-1 or currentRow == m-1):
                return steps
            for nextRow,nextCol in [(currentRow+1,currentCol),(currentRow-1,currentCol),(currentRow,currentCol+1),(currentRow,currentCol-1)]:
                if not(0<=nextRow<m and 0<=nextCol<n) or (nextRow,nextCol) in visited or maze[nextRow][nextCol] == '+':
                    continue
                visited.add((nextRow,nextCol))
                queue.append((nextRow,nextCol,steps+1))
            #print(queue)
        return -1

