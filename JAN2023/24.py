#attempt4:
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        for row in range(n//2):
            for col in range(n):
                board[row][col],board[n-1-row][col] = board[n-1-row][col],board[row][col]
        queue = deque([(0,0)])
        visited = {0}
        while(queue):
            value,steps = queue.popleft()
            if value == n*n-1:
                return steps
            for nextVal in range(value+1,min(value+6+1,n*n)):
                row = nextVal//n
                col = nextVal%n
                if row%2:
                    col = n-1-col
                if board[row][col] != -1:
                    nextVal = board[row][col]-1
                #print(nextVal,row,col)
                if nextVal not in visited:
                    visited.add(nextVal)
                    queue.append((nextVal,steps+1))
            #print(value,queue)
        return -1


#attempt3: Cache is not needed. The thing is you need to move from nextVal
#and calculate the next board location based on that
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        cache = {}
        n = len(board)
        for row in range(n//2):
            for col in range(n):
                board[row][col],board[n-1-row][col] = board[n-1-row][col],board[row][col]
        #print(board)
        for row in range(n):
            start = row*n
            end = row*n + n
            ahead = 1
            if row%2:
                start,end = end-1,start-1
                ahead = -1
            #print(row,start,end)
            for col in range(start,end,ahead):
                cache[col] = (row,col-(row*n))
        #print(cache)
        queue = deque([(0,0)])
        visited = {0}
        while(queue):
            value,steps = queue.popleft()
            if value == n*n-1:
                return steps
            for nextVal in range(value+1,min(value+6+1,n*n)):
                row = nextVal//n
                col = nextVal%n
                if row%2:
                    col = n-1-col
                if board[row][col] != -1:
                    nextVal = board[row][col]-1
                #print(nextVal,row,col)
                if nextVal not in visited:
                    visited.add(nextVal)
                    queue.append((nextVal,steps+1))
            #print(value,queue)
        return -1

#attempt2: WA: while going from currentval to nextval
'''
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        cache = {}
        n = len(board)
        for row in range(n//2):
            for col in range(n):
                board[row][col],board[n-1-row][col] = board[n-1-row][col],board[row][col]
        for row in range(n):
            start = row*n
            end = row*n + n
            ahead = 1
            if row%2:
                start,end = end-1,start-1
                ahead = -1
            for col in range(start,end,ahead):
                cache[col] = (row,col-start)
        #print(cache)
        queue = deque([(0,0)])
        visited = {0}
        while(queue):
            value,steps = queue.popleft()
            if value == n*n-1:
                return steps
            for nextVal in range(value+1,min(value+6+1,n*n)):
                row,col = cache[nextVal]
                if board[row][col] != -1:
                    nextVal = board[row][col]-1
                if nextVal not in visited:
                    visited.add(nextVal)
                    queue.append((nextVal,steps+1))
            #print(queue)
        return -1

'''

#attempt1: TLE because I used dfs, the concept was also wrong
