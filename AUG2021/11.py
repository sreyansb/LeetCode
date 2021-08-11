#attempt1:
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dino={}
        odds=[]
        
        for i in arr:
            if i&1:
                odds.append(i)
            if i not in dino:
                dino[i]=0
            dino[i]+=1
            
        for i in odds:
            if 2*i not in dino:
                return False
            dino[i]-=1
            dino[2*i]-=1
            if dino[2*i]==0:
                del dino[2*i]
            if dino[i]==0:
                del dino[i]
        #print(dino)
        
        for i in sorted(dino.keys(),key=lambda x:abs(x)):
            if i in dino:
                if 2*i not in dino or dino[2*i]<dino[i]:
                    return False
                
                if 2*i in dino:
                    dino[2*i]-=dino[i]
                del dino[i]
                if 2*i in dino and dino[2*i]==0:
                    del dino[2*i]
        
        return len(dino)==0
    
        
        