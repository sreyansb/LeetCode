#attempt2:
class Solution:
    def calculate(self, s: str) -> int:
        def divsolve(index,n,s,stack):
            nextarg = ""
            while(index<n and s[index].isdigit()):
                nextarg += s[index]
                index += 1
            stack.append(str(int(stack.pop())//int(nextarg)))
            return index
        
        def addsolve(index,n,s,stack):
            nextarg = ""
            while(index<n and s[index].isdigit()):
                nextarg += s[index]
                index += 1
            stack.append(str(int(stack.pop())+int(nextarg)))
            return index
        
        def subsolve(index,n,s,stack):
            nextarg = ""
            while(index<n and s[index].isdigit()):
                nextarg += s[index]
                index += 1
            stack.append(str(int(stack.pop())-int(nextarg)))
            return index
        
        def mulsolve(index,n,s,stack):
            nextarg = ""
            while(index<n and s[index].isdigit()):
                nextarg += s[index]
                index += 1
            stack.append(str(int(stack.pop())*int(nextarg)))
            return index
        
        def solve(s,char1,char2):
            stack = []
            n = len(s)
            index = 0
            while(index<n):
                i = s[index]
                if i.isdigit():
                    if stack and stack[-1].isdigit():
                        stack[-1] += i
                    else:
                        stack.append(i)
                    index += 1
                elif i == char1:
                    index += 1
                    if char1 == "/":
                        index = divsolve(index,n,s,stack)
                    elif char1 == '+':
                        index = addsolve(index,n,s,stack)
                    elif char1 == "-":
                        index = subsolve(index,n,s,stack)
                    else:
                        index = mulsolve(index,n,s,stack)
                elif i==char2:
                    index += 1
                    if char2 == "/":
                        index = divsolve(index,n,s,stack)
                    elif char2 == '+':
                        index = addsolve(index,n,s,stack)
                    elif char2 == "-":
                        index = subsolve(index,n,s,stack)
                    else:
                        index = mulsolve(index,n,s,stack)
                
                else:
                    stack.append(i)
                    index += 1
            return "".join(stack)
        
        s = s.replace(" ","")
        s = solve(s,"/","*")
        #print(s)
        #s = solve(s,"*")
        #print(s)
        s = solve(s,"+","-")
        #print(s)
        #s = solve(s,"-")
        #print(s)
        
        return int(s)

#attempt1: WA becoz I followed BODMAS and not left associativity
'''
class Solution:
    def calculate(self, s: str) -> int:
        def divsolve(index,n,s,stack):
            nextarg = ""
            while(index<n and s[index].isdigit()):
                nextarg += s[index]
                index += 1
            stack.append(str(int(stack.pop())//int(nextarg)))
            return index
        
        def addsolve(index,n,s,stack):
            nextarg = ""
            while(index<n and s[index].isdigit()):
                nextarg += s[index]
                index += 1
            stack.append(str(int(stack.pop())+int(nextarg)))
            return index
        
        def subsolve(index,n,s,stack):
            nextarg = ""
            while(index<n and s[index].isdigit()):
                nextarg += s[index]
                index += 1
            stack.append(str(int(stack.pop())-int(nextarg)))
            return index
        
        def mulsolve(index,n,s,stack):
            nextarg = ""
            while(index<n and s[index].isdigit()):
                nextarg += s[index]
                index += 1
            stack.append(str(int(stack.pop())*int(nextarg)))
            return index
        
        def solve(s,char):
            stack = []
            n = len(s)
            index = 0
            while(index<n):
                i = s[index]
                if i.isdigit():
                    if stack and stack[-1].isdigit():
                        stack[-1] += i
                    else:
                        stack.append(i)
                    index += 1
                elif i == char:
                    index += 1
                    if char == "/":
                        index = divsolve(index,n,s,stack)
                    elif char == '+':
                        index = addsolve(index,n,s,stack)
                    elif char == "-":
                        index = subsolve(index,n,s,stack)
                    else:
                        index = mulsolve(index,n,s,stack)
                
                else:
                    stack.append(i)
                    index += 1
            return "".join(stack)
        
        s = s.replace(" ","")
        s = solve(s,"/")
        #print(s)
        s = solve(s,"*")
        #print(s)
        s = solve(s,"+")
        #print(s)
        s = solve(s,"-")
        #print(s)
        
        return int(s)
        
'''
