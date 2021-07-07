#attempt2:
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans=[]
        for i in matrix:
            ans+=i
        ans.sort()
        return ans[k-1]

#attempt1: WA because row2 1st element can have smaller element than row 1 last element
#have to flatten the matrix
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        k-=1
        row=k//n
        col=k%n
        return matrix[row][col]
'''