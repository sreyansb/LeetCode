#attempt1:
class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        s=list(s)
        for i in range(len(s)):
            for j in range(i+1,min(i+3,len(s))):
                if s[j]==s[i]:
                    s[j]='*'
                else:
                    break
        #print(s)
        stack=[]
        for i in s[::-1]:
            if i=="*":
                stack.append(i)
                continue
            if stack:
                temp=d[i]
                while(stack and stack[-1]=='*'):
                    temp+=d[i]
                    stack.pop()
                if stack:
                    if stack[-1]<4:
                        ele=stack.pop()
                        stack.append(temp+ele)
                    elif stack[-1]<=d[i]:
                        ele=stack.pop()
                        stack.append(temp+ele)
                    else:
                        ele=stack.pop()
                        stack.append(ele-temp)
                else:
                    stack.append(temp)
            else:
                stack.append(d[i])
            #print(stack)
        return "".join([str(i) for i in stack])
                
                    
                    
                    
