#attempt1:
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        def count1s(row):
            i=0
            count=0
            while(i<n and mat[row][i]):
                count+=1
                i+=1
            return count 
        arrf=[]
        for i in range(m):
            arrf.append((count1s(i),i))
        arrf.sort(key=lambda x:(x[0],x[1]))
        return [x[1] for x in arrf[:k]]
        
