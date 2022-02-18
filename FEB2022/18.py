#attempt5: TOOK HELP : Exceptionally great soln using monotonic stack
#keep pushing in elements which are greater than stack top and keep top n-k elements
class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        numlen = len(s)
        if numlen==k:
            return "0"
        stack = []
        for i in s:
            while(stack and stack[-1]>i and k):
                stack.pop()
                k -= 1
            stack.append(i)
        while(k):
            stack.pop()
            k -= 1
        
        ans = "".join(stack).lstrip("0")
        if not(ans):
            ans = "0"
        return ans

#attempt4: WA we need to check if final answer is unempty
'''
class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        numlen = len(s)
        if numlen==k:
            return "0"
        stack = []
        for i in s:
            while(stack and stack[-1]>i and k):
                stack.pop()
                k -= 1
            stack.append(i)
        while(k):
            stack.pop()
            k -= 1
        return "".join(stack).lstrip("0")
'''

#attempt3: TOOK HELP: WA because we need to return "0" and not 0
'''
class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        numlen = len(s)
        if numlen==k:
            return 0
        stack = []
        for i in s:
            while(stack and stack[-1]>i and k):
                stack.pop()
                k -= 1
            stack.append(i)
        while(k):
            stack.pop()
            k -= 1
        return "".join(stack).lstrip("0")
'''

#attempt2: TOOK HELP: WA edge case we need only lstrip
'''
class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        numlen = len(s)
        if numlen==k:
            return 0
        stack = []
        for i in s:
            while(stack and stack[-1]>i and k):
                stack.pop()
                k -= 1
            stack.append(i)
        while(k):
            stack.pop()
            k -= 1
        return "".join(stack).strip("0")
'''

#attempt1:WA wrong idea because the elements removed can be separate
'''
class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        numlen = len(s)
        if numlen==k:
            return 0
        mini = float('inf')
        for index in range(0,numlen-k+1):
            #print(index,index+k)
            mini = min(mini,int(s[:index]+s[index+k:]))
        return str(mini)
'''
