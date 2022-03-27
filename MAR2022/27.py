#attempt1:
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        di = {}
        for i in range(len(mat)):
            di[i] = sum(mat[i])
        return sorted(di.keys(),key = lambda x:(di[x],x))[:k]
