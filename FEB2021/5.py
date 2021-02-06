#attempt1:
class Solution:
    def simplifyPath(self, path: str) -> str:
        path.strip("/")
        stack=[]
        for j in path.split("/"):
            if not(j) or j==".":
                continue
            elif j=="..":
                if not(stack):
                    continue
                else:
                    stack.pop()
            else:
                stack.append("/"+j)
        return "".join(stack) if stack else "/"
