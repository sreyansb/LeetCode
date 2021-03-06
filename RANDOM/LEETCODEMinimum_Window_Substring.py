#attempt2: We dont care about characters' positions, all we care is about
#if the string appears or not
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans=""
        leng=1000000
        left=0
        right=len(t)-1
        di={}
        for i in t:
            if i not in di:
                di[i]=0
            di[i]+=1
        dii={}
        for i in s[left:right+1]:
            if i not in dii:
                dii[i]=0
            dii[i]+=1
        def check():
            for i in di:
                if i not in dii or dii[i]<di[i]:
                    return False
            return True
        while(right<len(s)):
            #print(left,right,di,dii)
            if right-left+1<len(t):
                if left+len(t)-1<len(s)-1:
                    right=left+len(t)-1
                    for i in range(left,right+1):
                        if s[i] not in dii:
                            dii[s[i]]=0
                        dii[s[i]]+=1
                else:
                    break
            if check():
                if right-left+1<leng:
                    leng=right-left+1
                    ans=s[left:right+1]
                dii[s[left]]-=1
                if dii[s[left]]==0:
                    del dii[s[left]]
                left+=1
            else:
                right+=1
                if right<len(s):
                    if s[right] not in dii:
                        dii[s[right]]=0
                    dii[s[right]]+=1
        return ans

#attempt1:TLE
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans=""
        leng=1000000
        left=0
        right=len(t)-1
        di={}
        for i in t:
            if i not in di:
                di[i]=0
            di[i]+=1
        def check(l,r):
            dii={}
            for i in s[l:r+1]:
                if i not in dii:
                    dii[i]=0
                dii[i]+=1
            for i in di:
                if i not in dii or di[i]>dii[i]:
                    return False
            del dii
            return True
        while(right<len(s)):
            if right-left+1<len(t):
                if left+len(t)-1<len(s)-1:
                    right=left+len(t)-1
                else:
                    break
            if check(left,right):
                if right-left+1<leng:
                    leng=right-left+1
                    ans=s[left:right+1]
                left+=1
            else:
                right+=1
        return ans
'''
