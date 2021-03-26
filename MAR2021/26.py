#attempt1:
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ansl=[]
        ansb=[]
        for i in A:
            di={}
            for j in i:
                if j not in di:
                    di[j]=0
                di[j]+=1
            ansl.append(di)
            del di
        maindi={}
        for i in B:
            di={}
            for j in i:
                if j not in di:
                    di[j]=0
                di[j]+=1
            for i in di:
                if i not in maindi:
                    maindi[i]=0
                maindi[i]=max(maindi[i],di[i])            
            del di
        ans=[]
        for i in range(len(ansl)):
            flag=1
            for j in maindi:
                if j in ansl[i] and ansl[i][j]>=maindi[j]:
                    pass
                else:
                    flag=0
                    break
            if flag:
                ans.append(A[i])
        return ans
        
