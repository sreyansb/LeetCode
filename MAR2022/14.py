#attempt2:
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path[1:]
        path = path.strip("/")
        n = len(path)
        index = 0
        stack = ["/"]
        while(index<n):
            ele = path[index]
            if ele == "/":
                if stack and stack[-1]!="/":
                    stack.append("/")
                elif not(stack):
                    stack.append("/")
                while(index<n and path[index] == "/"):
                    index += 1
            elif ele.isalnum():
                startindex = index
                while(index<n and path[index]!="/"):
                    index += 1
                stack.append(path[startindex:index])
            else:
                number = 0
                while(index<n and path[index] == "."):
                    index += 1
                    number += 1
                word = "."*number
                while(index<n and path[index].isalnum()):
                    word += path[index]
                    index += 1
                if word == ".":
                    stack.pop()
                elif word == "..":
                    stack.pop()
                    if stack:
                        stack.pop()
                else:
                    stack.append(word)
                if not(stack):
                    stack.append("/")
            #print(stack)
        ans = "".join(stack).rstrip("/")
        return ans if ans else "/"

#attempt1: WA didn't take care of trailing slashes
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path[1:]
        path = path.strip("/")
        n = len(path)
        index = 0
        stack = ["/"]
        while(index<n):
            ele = path[index]
            if ele == "/":
                if stack and stack[-1]!="/":
                    stack.append("/")
                elif not(stack):
                    stack.append("/")
                while(index<n and path[index] == "/"):
                    index += 1
            elif ele.isalnum():
                startindex = index
                while(index<n and path[index]!="/"):
                    index += 1
                stack.append(path[startindex:index])
            else:
                number = 0
                while(index<n and path[index] == "."):
                    index += 1
                    number += 1
                word = "."*number
                while(index<n and path[index].isalnum()):
                    word += path[index]
                    index += 1
                if word == ".":
                    stack.pop()
                elif word == "..":
                    stack.pop()
                    if stack:
                        stack.pop()
                else:
                    stack.append(word)
                if not(stack):
                    stack.append("/")
            #print(stack)
        return "".join(stack)
'''
