#attempt1: TOOK HELP
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        stamp,target=list(stamp),list(target)
        stalen,tarlen=len(stamp),len(target)
        
        def check(start):
            flag=1
            for i in range(stalen):
                if stamp[i]!=target[i+start] and target[i+start]!='?':
                    flag=0
                    break
            if flag:
                flagy=0
                for i in range(stalen):
                    if target[i+start]!='?':
                        flagy=1
                        target[i+start]='?'
                if flagy:
                    return start
                return -1
            return -1
        
        ans=[]
        for i in range(tarlen-stalen+1):
            z=check(i)
            if z!=-1:
                ans.append(z)
        for i in range(tarlen-stalen,-1,-1):
            z=check(i)
            if z!=-1:
                ans.append(z)
        return ans[::-1] if set(target)=={'?'} else []
                    
        
        
