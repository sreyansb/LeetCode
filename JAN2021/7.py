#attempt n: Made many small errors like: all characters are accepted and not
#just alphabets, submitted many times before verifying
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not(s):
            return 0
        maxie=0
        index=0
        stack=[]
        while(index<len(s)):
            #print(s[index])
            if s[index] in stack:
                j=len(stack)-1
                while(j>=0):
                    if stack[j]==s[index]:
                        break
                    j-=1
                stack=stack[j+1:]
                stack.append(s[index])
            else:
                stack.append(s[index])
            maxie=max(maxie,len(stack))
            index+=1
            #print(stack)
        return maxie
        
