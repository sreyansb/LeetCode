#attempt2:
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        f=""
        stack=[]
        index=0
        for i in s:
            if i!="(" and i!=")":
                f=f+i
                index+=1
            else:
                if i=="(":
                    stack.append(index)
                    f=f+i
                    index+=1
                elif i==")":
                    if stack:
                        f=f+i
                        index+=1
                        stack.pop()
            #print(i,stack,f)
        notimes=0
        f=[f[i] for i in range(len(f)) if i not in stack]        
        return "".join(f)

#attempt1: WA
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        f=""
        stack=[]
        index=0
        for i in s:
            if i!="(" and i!=")":
                f=f+i
                index+=1
            else:
                if i=="(":
                    stack.append(index)
                    f=f+i
                    index+=1
                elif i==")":
                    if stack:
                        f=f+i
                        index+=1
                        stack.pop()
            #print(i,stack,f)
        notimes=0
        while(stack):
            ele=stack.pop()
            index=max(0,ele-notimes)
            #print(index)
            try:
                s=f[:index]
            except:
                pass
            try:
                s1=f[index+1:]
            except:
                pass
            f=s+s1
            notimes+=1
        return f
            
        
'''
