#attempt3: others WA
class Solution:
    def longestValidParentheses(self, s):
        stack=[]
        maxie=0
        lastop=0
        last=0
        i=0
        while(i<len(s)):
            #print(stack,last)
            if s[i]=='(':
                stack.append('i')
                last+=1
                i+=1
            else:
                cop=last-1
                if cop<0:
                    i+=1
                else:
                    flag=1
                    while(i<len(s) and s[i]==')' and cop>=0):
                        #print(stack)
                        if stack[cop]=='i':
                            flag=0
                            stack[cop]='v'
                            i+=1
                        cop-=1
                    if flag:
                        stack.append('w')
                        last+=1
                        i+=1
        #print(stack)
        n=len(stack)
        i=0
        curlen=0
        while(i<n):
            if stack[i]=='v':
                curlen+=2
            else:
                maxie=max(maxie,curlen)
                curlen=0
            i+=1
        return max(maxie,curlen)
