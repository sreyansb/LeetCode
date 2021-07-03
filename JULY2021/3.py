#attempt6:AC
from sortedcontainers import SortedList
from bisect import bisect_left,insort
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans=-float('inf')
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(1,n):
                matrix[i][j]+=matrix[i][j-1]
        for c1 in range(n):
            for c2 in range(c1,n):
                pastslist=[]
                curs=0
                for row in range(m):
                    insort(pastslist,curs)
                    curs+=matrix[row][c2]-(matrix[row][c1-1] if c1>0 else 0)
                    pos=bisect_left(pastslist,curs-k)
                    if pos!=len(pastslist):
                        ans=max(ans,curs-pastslist[pos])
        return ans

#attempt5: AC used insort instead of sortedlist
'''
from sortedcontainers import SortedList
from bisect import bisect_left
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans=-float('inf')
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(1,n):
                matrix[i][j]+=matrix[i][j-1]
        for c1 in range(n):
            for c2 in range(c1,n):
                pastslist=[]
                curs=0
                for row in range(m):
                    insort(pastslist,curs)
                    curs+=matrix[row][c2]-(matrix[row][c1-1] if c1>0 else 0)
                    pos=bisect_left(pastslist,curs-k)
                    if pos!=len(pastslist):
                        ans=max(ans,curs-pastslist[pos])
        return ans        
'''

#attempt4: TLE because usage of SortedList . Use insort of SOrtedList
'''
from sortedcontainers import SortedList
from bisect import bisect_left
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans=-float('inf')
        m=len(matrix)
        n=len(matrix[0])
        
        for c1 in range(n):
            if c1!=0:
                for row in range(m):
                    matrix[row][c1]+=matrix[row][c1-1]
            for c2 in range(c1+1):
                pastslist=SortedList([])
                curs=0
                for row in range(m):
                    pastslist.add(curs)
                    curs+=matrix[row][c1]-(matrix[row][c2-1] if c2>0 else 0)
                    pos=bisect_left(pastslist,curs-k)
                    if pos!=len(pastslist):
                        ans=max(ans,curs-pastslist[pos])
        return ans
'''


#attempt3: WA because I didnt maintain semantics in the changed configuration
'''
from sortedcontainers import SortedList
from bisect import bisect_left
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans=-float('inf')
        m=len(matrix)
        n=len(matrix[0])
        
        for c1 in range(n):
            if c1!=0:
                for row in range(m):
                    matrix[row][c1]=matrix[row][c1-1]+matrix[row][c1]
            for c2 in range(c1+1):
                pastslist=SortedList([])
                curs=0
                for row in range(m):
                    pastslist.add(curs)
                    curs+=matrix[row][c2]-(matrix[row][c1-1] if c1>0 else 0)
                    pos=bisect_left(pastslist,curs-k)
                    if pos!=len(pastslist):
                        ans=max(ans,curs-pastslist[pos])
        return ans
'''

#attempt2: TLE WE have to maintain a prefix sum array of 2D matrix for each row
#then for between two columns (O(c^2)) maintain a continuous sum between rows from start to end and
#binary search for current continuous sum - k
'''
from sortedcontainers import SortedList
from bisect import bisect_left
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans=-float('inf')
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(1,n):
                matrix[i][j]+=matrix[i][j-1]
        for c1 in range(n):
            for c2 in range(c1,n):
                pastslist=SortedList([])
                curs=0
                for row in range(m):
                    pastslist.add(curs)
                    curs+=matrix[row][c2]-(matrix[row][c1-1] if c1>0 else 0)
                    pos=bisect_left(pastslist,curs-k)
                    if pos!=len(pastslist):
                        ans=max(ans,curs-pastslist[pos])
        return ans
'''

#attempt1: WA I had some sort of idea:Prefix sum but dont know what I did
'''
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans=-float('inf')
        m=len(matrix)
        n=len(matrix[0])
        for row1 in range(m):
            for row2 in range(row1,m):
                cols=[0]*n
                for col in range(n):
                    cols[col]+=matrix[row2][col]
                    if cols[col]<=k:
                        ans=max(ans,cols[col])
                newcols=[cols[0]]*n
                for i in range(1,n):
                    newcols[i]=cols[i]+newcols[i-1]
                    if newcols[i]<=k:
                        ans=max(ans,newcols[i])
        return ans
'''