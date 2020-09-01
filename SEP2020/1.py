class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        s=[]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
                            if (A[i]>2) or (A[i]==2 and A[j]>3) or A[k]>5:
                                continue
                            s.append(str(A[i])+str(A[j])+":"+str(A[k])+str(A[l]))
        if s:
            return max(s)
        else:
            return ""
        
        
                
            
        
        
        
        
