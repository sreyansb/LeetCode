#attempt1:
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if not(stack) or stack[-1][0] != i:
                stack.append([i,1])
            else:
                if stack[-1][0] == i:
                    if stack[-1][1] == k-1:
                        stack.pop()
                    else:
                        stack[-1][1] += 1
        return "".join([i[0]*i[1] for i in stack])
            
        
        
