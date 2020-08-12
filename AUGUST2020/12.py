class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        s=[0]*(rowIndex+1)
        for i in range(rowIndex+1):
            for j in range(i,-1,-1):
                if j==0 or j==i:
                    s[j]=1
                else:
                    s[j]+=s[j-1]
        return s
                
        
