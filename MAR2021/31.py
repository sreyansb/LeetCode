#attempt1: TOOK HELP - you convert the target to '?'s and not the other way round

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        stamp,target=list(stamp),list(target)
        tarlen,stalen=len(target),len(stamp)
        
        def check(start):
            flag=1
            for i in range(stalen):
                if target[i+start]!='?' and stamp[i]!=target[i+start]:
                    flag=0
                    break
            if flag:
                condi=set(target[start:start+stalen])!={'?'}
                for i in range(stalen):
                    target[i+start]='?'
                return start if condi else -1
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
        return ans[::-1] if "".join(target)=='?'*tarlen else []
    #very important to return reverse ans and not just ans
