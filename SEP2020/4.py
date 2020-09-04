#Attempt1:99.27% speed
#Similar to scheduling problem
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not(S):
            return 0
        di={}
        for i in range(len(S)):
            if S[i] not in di:
                di[S[i]]=(i,i)
            di[S[i]]=(di[S[i]][0],i)
        values=sorted(di.values(),key=lambda x:x[0])
        final=[]
        ix=values[0][0]
        iy=values[0][1]
        for i in range(1,len(values)):
            if values[i][0]>iy:
                final.append(iy-ix+1)
                ix=values[i][0]
                iy=values[i][1]
            else:
                if values[i][1]>iy:
                    iy=values[i][1]
        final.append(iy-ix+1)
        return final
