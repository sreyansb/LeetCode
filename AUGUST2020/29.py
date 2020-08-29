from heapq import heapify,heappop
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        k=[-i for i in A]
        heapify(k)
        indexi=0
        final=[]
        #print(A,k)
        while(k):
            ele=-1*heappop(k)
            if A[ele-1]==ele:
                continue
            pos=A.index(ele)
            if pos:
                final.append(pos+1)
            A[:pos+1]=A[:pos+1][::-1]
            final.append(ele)
            A[:ele]=A[:ele][::-1]
            print(ele,A)
        print(A)
        return final
            
                
        
        
