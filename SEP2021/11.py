#attempt6: AC 
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        
        def calc(news):
            #print(news)
            if len(news)<3:
                return int("".join(news))
            if news[0]=='-':
                ans=-int(news[1])
                index=2
            else:
                ans=int(news[0])
                index=1
            for i in range(index,len(news),2):
                try:
                    ans=ans+int(news[i]+news[i+1])
                except:
                    ans=ans-int(news[i]+news[i+1][1:])
                #print(ans)
            #print(ans)
            return ans
                
        for i in s:
            if i==" ":
                continue
            if i==')':
                news=[]
                while(stack and stack[-1]!="("):
                    news+=[stack.pop()]
                stack.pop()
                news=news[::-1]
                stack.append(str(calc(news)))
            elif i in "1234567890":
                if stack and stack[-1][-1] in "1234567890":
                    stack[-1]+=i
                else:
                    stack.append(i)
            else:
                stack.append(i)
            #print(i,stack)
        return calc(stack)

#attempt4&5: Runtime Error Didn't take care of +-x/--x
'''
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        
        def calc(news):
            #print(news)
            if len(news)<3:
                return int("".join(news))
            if news[0]=='-':
                ans=-int(news[1])
                index=2
            else:
                ans=int(news[0])
                index=1
            for i in range(index,len(news),2):
                ans=ans+int(news[i]+news[i+1])
                #print(ans)
            #print(ans)
            return ans
                
        for i in s:
            if i==" ":
                continue
            if i==')':
                news=[]
                while(stack and stack[-1]!="("):
                    news+=[stack.pop()]
                stack.pop()
                news=news[::-1]
                stack.append(str(calc(news)))
            elif i in "1234567890":
                if stack and stack[-1][-1] in "1234567890":
                    stack[-1]+=i
                else:
                    stack.append(i)
            else:
                stack.append(i)
            #print(i,stack)
        return calc(stack)
'''


#attempt3: RUnTIme error: Didn't take care of "-2+ 1"
'''
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        
        def calc(news):
            #print(news)
            if len(news)<3:
                return int("".join(news))
            ans=int(news[0])
            for i in range(1,len(news),2):
                ans=ans+int(news[i]+news[i+1])
                #print(ans)
            #print(ans)
            return ans
                
        for i in s:
            if i==" ":
                continue
            if i==')':
                news=[]
                while(stack and stack[-1]!="("):
                    news+=[stack.pop()]
                stack.pop()
                news=news[::-1]
                stack.append(str(calc(news)))
            elif i in "1234567890":
                if stack and stack[-1][-1] in "1234567890":
                    stack[-1]+=i
                else:
                    stack.append(i)
            else:
                stack.append(i)
            #print(i,stack)
        return calc(stack)
'''



#attempt2: WA: Didn't take care of "2147483647"
'''
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        
        def calc(news):
            #print(news)
            if len(news)<3:
                return int("".join(news))
            ans=int(news[0])
            for i in range(1,len(news),2):
                ans=ans+int(news[i]+news[i+1])
                #print(ans)
            #print(ans)
            return ans
                
        for i in s:
            if i==" ":
                continue
            if i==')':
                news=[]
                while(stack and stack[-1]!="("):
                    news+=[stack.pop()]
                stack.pop()
                news=news[::-1]
                stack.append(str(calc(news)))
            elif i in "1234567890":
                if stack and stack[-1] in "1234567890":
                    stack[-1]+=i
                else:
                    stack.append(i)
            else:
                stack.append(i)
            #print(i,stack)
        return calc(stack)
'''

#attempt1: Runtime Error: Didn't take care of "0"
'''
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        
        def calc(news):
            #print(news)
            if len(news)<3:
                return int(news)
            ans=int(news[0])
            for i in range(1,len(news),2):
                ans=ans+int(news[i]+news[i+1])
                #print(ans)
            #print(ans)
            return ans
                
        for i in s:
            if i==" ":
                continue
            if i==')':
                news=[]
                while(stack and stack[-1]!="("):
                    news+=[stack.pop()]
                stack.pop()
                news=news[::-1]
                stack.append(str(calc(news)))
            elif i in "1234567890":
                if stack and stack[-1] in "1234567890":
                    stack[-1]+=i
                else:
                    stack.append(i)
            else:
                stack.append(i)
            #print(i,stack)
        return calc(stack)
'''