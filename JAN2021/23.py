#attempt2:
from heapq import heappush,heappop
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        di={}
        for i in range(m):
            for j in range(n):
                if i-j not in di:
                    di[i-j]=[]
                heappush(di[i-j],mat[i][j])
        for i in range(m):
            for j in range(n):
                mat[i][j]=heappop(di[i-j])
        return mat

#attempt1:
'''
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        di={}
        for i in range(m):
            for j in range(n):
                if i-j not in di:
                    di[i-j]=[[],0]
                di[i-j][0].append(mat[i][j])
        for i in di:
            di[i][0].sort()
        for i in range(m):
            for j in range(n):
                mat[i][j]=di[i-j][0][di[i-j][1]]
                di[i-j][1]+=1
        return mat
'''
