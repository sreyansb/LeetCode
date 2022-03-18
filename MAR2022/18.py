#attempt2 : TOOK HELP : No thinking capacity now
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        ans=[]
        di={}
        for i in s:
            if i not in di:
                di[i]=0
            di[i]+=1
        for i in s:
            di[i]-=1
            if i not in ans:
                while ans and ans[-1]>i and di[ans[-1]]>0:
                    ans.pop()
                ans.append(i)
        return "".join(ans)

#attempt1:WA
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        same_ele_ahead = [0]*n
        smaller_ele_ahead = [n]*n
        larger_ele_ahead = [n]*n
        final = ""
        chars_seen = {}
        for index in range(n-1,-1,-1):
            i = s[index]
            for char in chars_seen:
                if char<i:
                    smaller_ele_ahead[index] = min(chars_seen[char],smaller_ele_ahead[index])
                elif char>i:
                    larger_ele_ahead[index] = min(chars_seen[char],larger_ele_ahead[index])
            if i in chars_seen:
                same_ele_ahead[index] = 1
            else:
                chars_seen[i] = n
            chars_seen[i] = index
        
        for index in range(n):
            if same_ele_ahead[index]==0 or smaller_ele_ahead[index]>larger_ele_ahead[index]:
                if s[index] not in final:
                    final += s[index]
        return final
'''
