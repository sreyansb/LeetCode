#attempt6: DIrty SOlution
'''
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.match("^"+p+"$",s)
'''

#attempt5: AC
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen = len(s)
        plen = len(p)
        @lru_cache(None)
        def matchit(index1,index2):
            #print(index1,index2)
            if (index1==slen):
                if index2==plen:
                    return True
                if "*" in set(p[index2:index2+2]):
                    return matchit(index1,index2+2)
                return False
            if index2==plen:
                return index1==slen
            if p[index2]==".":
                ans = False
                if index2+1<plen:
                    if p[index2+1] == "*":
                        i = index1-1
                        while(i<slen):
                            ans = matchit(i+1,index2+2)
                            if ans:
                                return ans
                            i += 1
                        return False
                return matchit(index1+1,index2+1)
                            
            elif p[index2] != "*":
                if index2+1<plen:
                    if p[index2+1]=="*":
                        ans = False
                        ans = matchit(index1,index2+2)
                        if not(ans):
                            i = index1
                            while(i<slen and s[i] == p[index2]):
                                ans = matchit(i+1,index2+2)
                                if ans:
                                    break
                                i += 1
                        return ans
                return s[index1]==p[index2] and matchit(index1+1,index2+1)
            
            return False
                        
                 
        return matchit(0,0)
                        

#attempt4: WA wrongly handled, shouldve looked at index2+2
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen = len(s)
        plen = len(p)
        @lru_cache(None)
        def matchit(index1,index2):
            #print(index1,index2)
            if (index1==slen):
                #print("2o",index2)
                return index2==plen
            if index2==plen:
                #print("1o",index1)
                return index1==slen
            if p[index2]==".":
                ans = False
                if index2+1<plen:
                    if p[index2+1] == "*":
                        i = index1-1
                        while(i<slen):
                            ans = matchit(i+1,index2+2)
                            if ans:
                                return ans
                            i += 1
                        return False
                return matchit(index1+1,index2+1)
                            
            elif p[index2] != "*":
                if index2+1<plen:
                    if p[index2+1]=="*":
                        ans = False
                        ans = matchit(index1,index2+2)
                        if not(ans):
                            i = index1
                            while(i<slen and s[i] == p[index2]):
                                ans = matchit(i+1,index2+2)
                                i += 1
                                if ans:
                                    break
                        return ans
                return s[index1]==p[index2] and matchit(index1+1,index2+1)
            
            return False
                        
                 
        return matchit(0,0)
                        
'''

#attempt3: WA because return True condition is terrible
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen = len(s)
        plen = len(p)
        @lru_cache(None)
        def matchit(index1,index2):
            #print(index1,index2)
            if (index1==slen):
                return index2==plen or (len(set(p[index2:]))<=2 and "*" in set(p[index2:]))
            if index2==plen:
                return index1==slen
            if p[index2]==".":
                ans = False
                if index2+1<plen:
                    if p[index2+1] == "*":
                        i = index1-1
                        while(i<slen):
                            ans = matchit(i+1,index2+2)
                            if ans:
                                return ans
                            i += 1
                        return False
                return matchit(index1+1,index2+1)
                            
            elif p[index2] != "*":
                if index2+1<plen:
                    if p[index2+1]=="*":
                        ans = False
                        ans = matchit(index1,index2+2)
                        if not(ans):
                            i = index1
                            while(i<slen and s[i] == p[index2]):
                                ans = matchit(i+1,index2+2)
                                i += 1
                                if ans:
                                    break
                        return ans
                return s[index1]==p[index2] and matchit(index1+1,index2+1)
            
            return False
                        
                 
        return matchit(0,0)
'''

#attempt2: WA 341/353
#Didn't take care of case when slen is breached but not plen
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen = len(s)
        plen = len(p)
        @lru_cache(None)
        def matchit(index1,index2):
            #print(index1,index2)
            if (index1==slen):
                return index2==plen or (len(set(p[index2:]))<=2 and "*" in set(p[index2:]))
            if index2==plen:
                return index1==slen
            if p[index2]==".":
                ans = False
                if index2+1<plen:
                    if p[index2+1] == "*":
                        i = index1-1
                        while(i<slen):
                            ans = matchit(i+1,index2+2)
                            if ans:
                                return ans
                            i += 1
                return matchit(index1+1,index2+1)
                            
            elif p[index2] != "*":
                if index2+1<plen:
                    if p[index2+1]=="*":
                        ans = False
                        ans = matchit(index1,index2+2)
                        if not(ans):
                            i = index1
                            while(i<slen and s[i] == p[index2]):
                                ans = matchit(i+1,index2+2)
                                i += 1
                                if ans:
                                    break
                        return ans
                return s[index1]==p[index2] and matchit(index1+1,index2+1)
            
            return False
        return matchit(0,0)
'''

#attempt1: WA 337/353:
#because didn't take care of * after .
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen = len(s)
        plen = len(p)
        @lru_cache(None)
        def matchit(index1,index2):
            #print(index1,index2)
            if (index1==slen):
                return index2==plen or (len(set(p[index2:]))<=2 and "*" in set(p[index2:]))
            if index2==plen:
                return index1==slen
            if p[index2]==".":
                ans = False
                if index2+1<plen:
                    if p[index2+1] == "*":
                        i = index1
                        while(i<slen):
                            ans = matchit(i+1,index2+2)
                            if ans:
                                return ans
                            i += 1
                return matchit(index1+1,index2+1)
                            
            elif p[index2] != "*":
                if index2+1<plen:
                    if p[index2+1]=="*":
                        ans = False
                        ans = matchit(index1,index2+2)
                        if not(ans):
                            i = index1
                            while(i<slen and s[i] == p[index2]):
                                ans = matchit(i+1,index2+2)
                                i += 1
                                if ans:
                                    break
                        return ans
                return s[index1]==p[index2] and matchit(index1+1,index2+1)
            
            return False
                        
                 
        return matchit(0,0)
                        
'''