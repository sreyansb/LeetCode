#attempt7: AC Too over engineered. We could easily do without replace and all
class Solution:
    def numDecodings(self, s: str) -> int:
        
        s=s.replace("*0","?").replace("10","o").replace("20","o")#? represents 2 ways, o represents only one way is there to frame the string
        mod=1000000007
        n=len(s)
        #print(s)
        @lru_cache(None)
        def recurse(index):
            
            if index>=n:
                return 1
            if s[index]=="0":
                return 0
            ans=1
            if s[index]=="?":
                ans=2*recurse(index+1)
                return ans%mod
            if s[index]=="o":
                ans= recurse(index+1)
                return ans%mod
            if index+1<n:
                if s[index]=='1':
                    if s[index+1]!='0':
                        if s[index+1] in ["?","o"]:
                            return recurse(index+1)
                        if s[index+1]=='*':
                            ans=recurse(index+1)+9*recurse(index+2)
                            if index+2<n and s[index+2]=='0':
                                ans=2*recurse(index+3)
                        else:
                            ans=recurse(index+1)+recurse(index+2)
                    else:
                        ans=recurse(index+2)
                elif s[index]=='2':
                    if s[index+1]!='0':
                        if s[index+1] in ["?","o"]:
                            return recurse(index+1)
                        if s[index+1]=='*':
                            ans=recurse(index+1)+6*recurse(index+2)
                        else:
                            if int(s[index+1])<7:
                                ans=recurse(index+1)+recurse(index+2)
                            else:
                                ans=recurse(index+1)
                    else:
                        ans=recurse(index+2)
                elif s[index]=='*':
                    if s[index+1]!='0':
                        if s[index+1] in ["?","o"]:
                            return 9*recurse(index+1)
                        if s[index+1]=='*':
                            ans=9*recurse(index+1)+15*recurse(index+2)
                        else:
                            if int(s[index+1])<7:
                                ans=+9*recurse(index+1)+2*recurse(index+2)
                            else:
                                ans=+9*recurse(index+1)+1*recurse(index+2)
                    else:
                        ans=2*recurse(index+2)
                else:
                    ans=recurse(index+1)
                return ans%mod
            else:
                if s[index]=='*':
                    return 9
                if s[index]=="?":
                    return 2
                return 1
        return recurse(0)%(1000000007)

#attempt5&6: Runtime Error and Memory Error: ALways MOD AT EACH STEP
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        
        s=s.replace("*0","?").replace("10","o").replace("20","o")
        n=len(s)
        #print(s)
        @lru_cache(None)
        def recurse(index):
            
            if index>=n:
                return 1
            if s[index]=="0":
                return 0
            ans=1
            if s[index]=="?":
                ans=2*recurse(index+1)
                return ans
            if s[index]=="o":
                return recurse(index+1)
            if index+1<n:
                if s[index]=='1':
                    if s[index+1]!='0':
                        if s[index+1] in ["?","o"]:
                            return recurse(index+1)
                        if s[index+1]=='*':
                            ans=recurse(index+1)+9*recurse(index+2)
                            if index+2<n and s[index+2]=='0':
                                ans=2*recurse(index+3)
                        else:
                            ans=recurse(index+1)+recurse(index+2)
                    else:
                        ans=recurse(index+2)
                elif s[index]=='2':
                    if s[index+1]!='0':
                        if s[index+1] in ["?","o"]:
                            return recurse(index+1)
                        if s[index+1]=='*':
                            ans=recurse(index+1)+6*recurse(index+2)
                            if index+2<n and s[index+2]=='0':
                                ans=2*recurse(index+3)
                        else:
                            if int(s[index+1])<7:
                                ans=recurse(index+1)+recurse(index+2)
                            else:
                                ans=recurse(index+1)
                    else:
                        ans=recurse(index+2)
                elif s[index]=='*':
                    if s[index+1]!='0':
                        if s[index+1] in ["?","o"]:
                            return 9*recurse(index+1)
                        if s[index+1]=='*':
                            ans=9*recurse(index+1)+15*recurse(index+2)
                        else:
                            if int(s[index+1])<7:
                                ans=9*recurse(index+1)+2*recurse(index+2)
                            else:
                                ans=9*recurse(index+1)+1*recurse(index+2)
                    else:
                        ans=2*recurse(index+2)
                else:
                    ans=recurse(index+1)
                return ans
            else:
                if s[index]=='*':
                    return 9
                if s[index]=="?":
                    return 2
                return 1
        return recurse(0)%(1000000007)
'''

#attempt4: WA Thought that they wont give a string where a number greater than 2 is followed  by a 0
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        
        s=s.replace("*0","?").replace("10","o").replace("20","o")
        n=len(s)
        print(s)
        @lru_cache(None)
        def recurse(index):
            if index>=n:
                return 1
            ans=1
            if s[index]=="?":
                ans=2*recurse(index+1)
                return ans
            if s[index]=="o":
                return recurse(index+1)
            if index+1<n:
                if s[index]=='1':
                    if s[index+1]!='0':
                        if s[index+1] in ["?","o"]:
                            return recurse(index+1)
                        if s[index+1]=='*':
                            ans=recurse(index+1)+9*recurse(index+2)
                            if index+2<n and s[index+2]=='0':
                                ans=2*recurse(index+3)
                        else:
                            ans=recurse(index+1)+recurse(index+2)
                    else:
                        ans=recurse(index+2)
                elif s[index]=='2':
                    if s[index+1]!='0':
                        if s[index+1] in ["?","o"]:
                            return recurse(index+1)
                        if s[index+1]=='*':
                            ans=recurse(index+1)+6*recurse(index+2)
                            if index+2<n and s[index+2]=='0':
                                ans=2*recurse(index+3)
                        else:
                            if int(s[index+1])<7:
                                ans=recurse(index+1)+recurse(index+2)
                            else:
                                ans=recurse(index+1)
                    else:
                        ans=recurse(index+2)
                elif s[index]=='*':
                    if s[index+1]!='0':
                        if s[index+1] in ["?","o"]:
                            return 9*recurse(index+1)
                        if s[index+1]=='*':
                            ans=9*recurse(index+1)+15*recurse(index+2)
                        else:
                            if int(s[index+1])<7:
                                ans=9*recurse(index+1)+2*recurse(index+2)
                            else:
                                ans=9*recurse(index+1)+1*recurse(index+2)
                    else:
                        ans=2*recurse(index+2)
                else:
                    ans=recurse(index+1)
                return ans
            else:
                if s[index]=='*':
                    return 9
                if s[index]=="?":
                    return 2
                return 1
        return recurse(0)%(1000000007)
'''

#attempt3: WA A long approach still couldn't get all cases for 0
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        
        s=s.replace("*0","?")
        n=len(s)
        print(s)
        @lru_cache(None)
        def recurse(index):
            if index>=n:
                return 1
            ans=1
            if s[index]=="?":
                ans=2*recurse(index+1)
                return ans
            if index+1<n:
                if s[index]=='1':
                    if s[index+1]!='0':
                        if s[index+1]=="?":
                            return recurse(index+1)
                        if s[index+1]=='*':
                            ans=recurse(index+1)+9*recurse(index+2)
                            if index+2<n and s[index+2]=='0':
                                ans=2*recurse(index+3)
                        else:
                            ans=recurse(index+1)+recurse(index+2)
                    else:
                        ans=recurse(index+2)
                elif s[index]=='2':
                    if s[index+1]!='0':
                        if s[index+1]=="?":
                            return recurse(index+1)
                        if s[index+1]=='*':
                            ans=recurse(index+1)+6*recurse(index+2)
                            if index+2<n and s[index+2]=='0':
                                ans=2*recurse(index+3)
                        else:
                            if int(s[index+1])<7:
                                ans=recurse(index+1)+recurse(index+2)
                            else:
                                ans=recurse(index+1)
                    else:
                        ans=recurse(index+2)
                elif s[index]=='*':
                    if s[index+1]!='0':
                        if s[index+1]=="?":
                            return 9*recurse(index+1)
                        if s[index+1]=='*':
                            ans=9*recurse(index+1)+15*recurse(index+2)
                        else:
                            if int(s[index+1])<7:
                                ans=9*recurse(index+1)+2*recurse(index+2)
                            else:
                                ans=9*recurse(index+1)+1*recurse(index+2)
                    else:
                        ans=2*recurse(index+2)
                else:
                    ans=recurse(index+1)
                return ans
            else:
                if s[index]=='*':
                    return 9
                if s[index]=="?":
                    return 2
                return 1
        return recurse(0)%(1000000007)        
'''

#attempt2: WA Didnt take into account how 0 work
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        s.replace("*0","?")
        @lru_cache(None)
        def recurse(index):
            if index>=n:
                return 1
            ans=1
            if s[index]=="?":
                ans=recurse(index+1)
                return ans
            if index+1<n:
                if s[index]=='1':
                    if s[index+1]!='0':
                        if s[index+1]=='*':
                            ans=recurse(index+1)+9*recurse(index+2)
                            if index+2<n and s[index+2]=='0':
                                ans=2*recurse(index+3)
                        else:
                            ans=recurse(index+1)
                    else:
                        ans=recurse(index+2)
                elif s[index]=='2':
                    if s[index+1]!='0':
                        if s[index+1]=='*':
                            ans=recurse(index+1)+6*recurse(index+2)
                            if index+2<n and s[index+2]=='0':
                                ans=2*recurse(index+3)
                        else:
                            if int(s[index+1])<7:
                                ans=recurse(index+1)+recurse(index+2)
                            else:
                                ans=recurse(index+1)
                    else:
                        ans=recurse(index+2)
                elif s[index]=='*':
                    if s[index+1]!='0':
                        if s[index+1]=='*':
                            ans=9*recurse(index+1)+15*recurse(index+2)
                        else:
                            if int(s[index+1])<7:
                                ans=9*recurse(index+1)+2*recurse(index+2)
                            else:
                                ans=9*recurse(index+1)+1*recurse(index+2)
                    else:
                        ans=2*recurse(index+2)
                else:
                    ans=recurse(index+1)
                return ans
            else:
                if s[index]=='*':
                    return 9
                return 1
        return recurse(0)%(1000000007)
'''

#attempt1: WA we need to go from back and solve group them together
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        @lru_cache(None)
        def recurse(index):
            if index>=n:
                return 1
            ans=1
            if index+1<n:
                if s[index]=='1':
                    if s[index+1]!='0':
                        if s[index+1]=='*':
                            ans=recurse(index+1)+9*recurse(index+2)
                            if index+2<n and s[index+2]=='0':
                                ans=2*recurse(index+3)
                        else:
                            ans=recurse(index+1)
                    else:
                        ans=recurse(index+2)
                elif s[index]=='2':
                    if s[index+1]!='0':
                        if s[index+1]=='*':
                            ans=recurse(index+1)+6*recurse(index+2)
                            if index+2<n and s[index+2]=='0':
                                ans=2*recurse(index+3)
                        else:
                            if int(s[index+1])<7:
                                ans=recurse(index+1)+recurse(index+2)
                            else:
                                ans=recurse(index+1)
                    else:
                        ans=recurse(index+2)
                elif s[index]=='*':
                    if s[index+1]!='0':
                        if s[index+1]=='*':
                            ans=9*recurse(index+1)+15*recurse(index+2)
                        else:
                            if int(s[index+1])<7:
                                ans=9*recurse(index+1)+2*recurse(index+2)
                            else:
                                ans=9*recurse(index+1)+1*recurse(index+2)
                    else:
                        ans=2*recurse(index+2)
                else:
                    ans=recurse(index+1)
                return ans
            else:
                if s[index]=='*':
                    return 9
                return 1
        return recurse(0)%(1000000007)
'''