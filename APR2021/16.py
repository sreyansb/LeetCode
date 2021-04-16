#attempt1:
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not(s):
            return ""
        stack=[]
        index=0
        n=len(s)
        while(index<n):
            if not stack:
                stack.append([s[index],1])
            else:
                if stack[-1][0]==s[index]:
                    stack[-1][1]+=1
                    if stack[-1][1]==k:
                        stack.pop()
                else:
                    stack.append([s[index],1])
            index+=1
        if not(stack):
            return ""
        return "".join([x[0]*x[1] for x in stack])
                
        
