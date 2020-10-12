class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        n=len(A)
        i=0
        wrong=[]
        wrongno=0
        diA={}
        diB={}
        while(i<n):
            if A[i] not in diA:
                diA[A[i]]=set()
            diA[A[i]].add(i)
            if B[i] not in diB:
                diB[B[i]]=set()
            diB[B[i]].add(i)
            if A[i]==B[i]:
                i+=1
                continue
            else:
                wrong.append(i)
                wrongno+=1
                if wrongno>2:
                    return False
                if wrongno==2:
                    if A[wrong[0]]!=B[wrong[1]] or A[wrong[1]]!=B[wrong[0]]:
                        return False
                i+=1
        #print(wrong)
        if wrongno==0:
            for i in diA:
                if i in diB:
                    if len(diA[i]&diB[i])>=2:
                        return True
        elif wrongno==2:
            return True
        else:
            return False
        
            
                        
                
