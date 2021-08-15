#attempt3:
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dit={}
        dis={}
        #print(s,t,s1)
        for i in t:
            if i not in dit:
                dit[i]=0
            dit[i]+=1
        
        
        def check(dis,dit):
            for i in dit:
                if i not in dis or dis[i]<dit[i]:
                    return False
            return True
        
        
        left,right,dis=0,0,{}
        flag=1
        while(right<len(s)):
            if s[right] not in dis:
                dis[s[right]]=0
            dis[s[right]]+=1
            if check(dis,dit):
                flag=0
                break
            right+=1
        if flag:
            return ""
        
        ans=s[left:right+1]
        minl=right-left+1
        while(right<len(s)):
            #print(left,right)
            dis[s[left]]-=1
            if check(dis,dit):
                left+=1
                if right-left+1<minl:
                    minl=right-left+1
                    ans=s[left:right+1]
            else:
                dis[s[left]]+=1
                right+=1
                if right<len(s):
                    if s[right] not in dis:
                        dis[s[right]]=0
                    dis[s[right]]+=1
        return ans

#attempt 1&2: WA and TLE
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dit={}
        dis={}
        for i in t:
            if i not in dit:
                dit[i]=0
            dit[i]+=1
        for i in s:
            if i not in dis:
                dis[i]=0
            dis[i]+=1
        start=0
        end=len(s)-1
        
        def check(dis,dit):
            for i in dit:
                if i not in dis or dis[i]<dit[i]:
                    return False
            return True
        ans=""
        if check(dis,dit):
            ans=s[start:end+1]
        else:
            return ""
        while(start<=end):
            dis[s[start]]-=1
            if check(dis,dit):
                start+=1
                ans=s[start:end+1]
            else:
                dis[s[start]]+=1
                start-=1
                dis[s[end]]-=1
                end-=1
                if check(dis,dit):
                    ans=s[start:end+1]
                else:
                    end+=1
                    break
        return ans        
'''
