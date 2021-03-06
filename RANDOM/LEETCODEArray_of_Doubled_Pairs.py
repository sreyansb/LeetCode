#attempt2:
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        n=len(arr)
        odds={}
        oddcount=0
        evens={}
        for i in arr:
            if i%2:
                if i not in odds:
                    odds[i]=0
                odds[i]+=1
                oddcount+=1
            else:
                if i not in evens:
                    evens[i]=0
                evens[i]+=1
        if oddcount>n//2:
            return False
        #print(evens)
        for i in odds:
            if 2*i not in evens or evens[2*i]<odds[i] :
                return False
            else:
                evens[2*i]-=odds[i]
        #we have all even numbers which haven't been used up by odd numbers
        #print(evens)
        posi={}
        nega={}
        posic=0
        negac=0
        for i in evens:
            if i>0 and evens[i]:
                posi[i]=evens[i]
                posic+=evens[i]
            elif i<0 and evens[i]:
                nega[i]=evens[i]
                negac+=evens[i]
            else:
                if evens[i]%2:
                    return False
        if posic%2 or negac%2:
            return False
        pose=sorted(posi)
        nege=sorted(nega,reverse=True)
        #print(posi,nega)
        for i in pose:
            if posi[i]:
                if 2*i not in posi or posi[2*i]<=0:
                    return False
                if posi[i]-posi[2*i]>0:
                    return False
                posi[2*i]=max(0,posi[2*i]-posi[i])
                #print(i,posi)
        #print(nega)
        for i in nege:
            if nega[i]:
                if 2*i not in nega or nega[2*i]<=0:
                    return False
                if nega[i]-nega[2*i]>0:
                    return False
                nega[2*i]=max(0,nega[2*i]-nega[i])
        return True

#attempt1: WA didnt take into consideration that some elements of the half
#would be reduced to 0
'''
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        n=len(arr)
        odds={}
        oddcount=0
        evens={}
        for i in arr:
            if i%2:
                if i not in odds:
                    odds[i]=0
                odds[i]+=1
                oddcount+=1
            else:
                if i not in evens:
                    evens[i]=0
                evens[i]+=1
        if oddcount>n//2:
            return False
        for i in odds:
            if 2*i not in evens or evens[2*i]<odds[i] :
                return False
            else:
                evens[2*i]-=odds[i]
        #we have all even numbers which haven't been used up by odd numbers
        for i in evens:
            if evens[i]:
                if 2*i in evens:
                    diff=max(0,min(evens[2*i],evens[i]))
                    evens[2*i]-=diff
                    if i!=2*i:
                        evens[i]-=diff
        for i in evens:
            if evens[i]:
                return False
        return True
                
        
                
'''

            
        
                
