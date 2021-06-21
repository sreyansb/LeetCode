#attempt1:
class Solution:
    def generate(self, numrows: int) -> List[List[int]]:
        ans=[[1]]
        for i in range(2,numrows+1):
            newrow=[1]
            for j in range(1,i-1):
                newrow.append(ans[-1][j-1]+ans[-1][j])
            newrow.append(1)
            ans.append(newrow.copy())
            del newrow
        return ans
                
            
        