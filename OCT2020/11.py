#attempt 3 90%
#took help
#if a character appears more than once we can see that it can get displaced
#so if ans mein last character ki count >0 (it will repeat) hai aur woh current character
#se bada hai i.e. ascii(ans[-1])>ascii(character), we can remove the stack ka last element
# and keep doing that util we find suitable position for the current character

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        ans=[]
        di={}
        for i in s:
            if i not in di:
                di[i]=0
            di[i]+=1
        for i in s:
            di[i]-=1
            if i not in ans:
                while ans and ans[-1]>i and di[ans[-1]]>0:
                    ans.pop()
                ans.append(i)
        return "".join(ans)

#attempt2: Wrong 275
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ans=[]
        for i in range(len(s)):
            if s[i] not in ans:
                ans.append(s[i])
            else:
                k=ans.copy()
                k.remove(s[i])
                k.append(s[i])
                if "".join(k)<"".join(ans):
                    ans=k.copy()
        return "".join(ans)
"""             
                
            
            

#attempt1: Wrong 130
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        return "".join(sorted(set(s)))
"""
