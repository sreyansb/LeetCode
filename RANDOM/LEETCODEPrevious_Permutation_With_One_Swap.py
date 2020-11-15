#attempt2: took help -> Johnson Trotter algo
class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        #print(A)
        if not(A) or A==sorted(A):
            return A
        number=int("".join([str(i) for i in A]))
        maxi=0
        arr=A.copy()
        n=len(A)-1
        i=n
        while(i>0):
            if A[i-1]>A[i]:
                break
            i-=1
        j=n
        while(j>=i):
            if A[j]<A[i-1]:
                break
            j-=1
        A[i-1],A[j]=A[j],A[i-1]
        #print(i,j,A)
        return A

#attempt1: WA
"""
class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        if not(A) or A==sorted(A):
            return A
        number=int("".join([str(i) for i in A]))
        maxi=0
        arr=A.copy()
        n=len(A)-1
        for i in range(n,0,-1):
            for j in range(i-1,-1,-1):
                if A[j]>A[i]:
                    A[j],A[i]=A[i],A[j]
                    x=int("".join([str(i) for i in A]))
                    if x>number:
                        A[j],A[i]=A[i],A[j]
                        continue
                    maxi=max(maxi,x)
                    if maxi==x:
                        arr=A.copy()
                    A[j],A[i]=A[i],A[j]
                    
        return arr
            
        
        
        
"""
