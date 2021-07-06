#attempt1:
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        di={}
        tot=0
        for i in arr:
            if i not in di:
                di[i]=0
            di[i]+=1
            tot+=1
        l=sorted(di,reverse=True,key=lambda x:di[x])
        ans=0
        curlen=tot
        index=0
        while(curlen>(tot+1)//2):
            ans+=1
            curlen-=di[l[index]]
            index+=1
        return ans
        