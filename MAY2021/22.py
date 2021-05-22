#attempt2: After 3 hours: AC: We dont need the flag part because somehow if the flag condition is not met the thing will be traversed in the loops
#instead of dp thing doing O(n^2) we could simply run a loop based on properties of the diagonals
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n==1:
            return [["Q"]]
        if n==2:
            return []
        ans=[]
        def check(row,col,board,dp,currentnodes):
            if row>=n:
                ans.append(["".join(i) for i in board])
                return True
            else:
                flag=1
                for i in range(col,n):
                    if dp[row][i]==0:
                        flag=0
                        board[row][i]='Q'
                        currentnodes.append((row,i))
                        dp[row][i]=1
                        for j in range(n):
                            dp[row][j]+=1
                            dp[j][i]+=1
                        for r in range(n):
                            for c in range(n):
                                if r+c==row+i:
                                    dp[r][c]+=1
                                if r-c==row-i:
                                    dp[r][c]+=1
                        ansk=check(row+1,0,board,dp,currentnodes)
                        dp[row][i]=0
                        board[row][i]="."
                        for j in range(n):
                            dp[row][j]-=1
                            dp[j][i]-=1
                            dp[row][j]=max(0,dp[row][j])
                            dp[j][i]=max(0,dp[j][i])
                        for r in range(n):
                            for c in range(n):
                                if r+c==row+i:
                                    dp[r][c]-=1
                                    dp[r][c]=max(0,dp[r][c])
                                if r-c==row-i:
                                    dp[r][c]-=1
                                    dp[r][c]=max(0,dp[r][c])
                        if currentnodes:
                            currentnodes.pop()
                
        dp=[[0 for i in range(n)]for j in range(n)]
        board=[["." for i in range(n)]for j in range(n)]
        check(0,0,board,dp,[])
        return ans

#attempt1: TLE
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n==1:
            return [["Q"]]
        if n==2:
            return []
        ans=[]
        def check(row,col,board,dp,currentnodes):
            if row>=n:
                ans.append(["".join(i) for i in board])
                return True
            else:
                flag=1
                for i in range(col,n):
                    if dp[row][i]==0:
                        flag=0
                        board[row][i]='Q'
                        currentnodes.append((row,i))
                        dp[row][i]=1
                        for j in range(n):
                            dp[row][j]+=1
                            dp[j][i]+=1
                        for r in range(n):
                            for c in range(n):
                                if r+c==row+i:
                                    dp[r][c]+=1
                                if r-c==row-i:
                                    dp[r][c]+=1
                        ansk=check(row+1,0,board,dp,currentnodes)
                        dp[row][i]=0
                        board[row][i]="."
                        for j in range(n):
                            dp[row][j]-=1
                            dp[j][i]-=1
                            dp[row][j]=max(0,dp[row][j])
                            dp[j][i]=max(0,dp[j][i])
                        for r in range(n):
                            for c in range(n):
                                if r+c==row+i:
                                    dp[r][c]-=1
                                    dp[r][c]=max(0,dp[r][c])
                                if r-c==row-i:
                                    dp[r][c]-=1
                                    dp[r][c]=max(0,dp[r][c])
                        if currentnodes:
                            currentnodes.pop()
                if flag:
                    if not currentnodes:
                        return False
                    rowj,i=currentnodes.pop()
                    board[rowj][i]="."
                    dp[rowj][i]-=1
                    dp[rowj][i]=max(0,dp[rowj][i])
                    for j in range(n):
                            dp[rowj][j]-=1
                            dp[j][i]-=1
                            dp[rowj][j]=max(0,dp[rowj][j])
                            dp[j][i]=max(0,dp[j][i])
                    for r in range(n):
                        for c in range(n):
                            if r+c==rowj+i:
                                dp[r][c]-=1
                                dp[r][c]=max(0,dp[r][c])
                            if r-c==rowj-i:
                                dp[r][c]-=1
                                dp[r][c]=max(0,dp[r][c])
                    return check(rowj,i+1,board,dp,currentnodes)
                else:
                    return ansk
        dp=[[0 for i in range(n)]for j in range(n)]
        board=[["." for i in range(n)]for j in range(n)]
        check(0,0,board,dp,[])
        return ans
'''