#attempt2: 656ms by using Performance Engineering principles
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        def recurse(index,current_words):
            if index>=n:
                ans.append(current_words.copy())
                return
            for new_index in range(index+1,n+1):
                word = s[index:new_index]
                if word == word[::-1]:
                    recurse(new_index,current_words+[s[index:new_index]])
        recurse(0,[])
        return ans

#attempt1: 1169ms naive algo
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        def recurse(index,current_words):
            if index>=n:
                ans.append(current_words.copy())
                return
            for new_index in range(index+1,n+1):
                if s[index:new_index] == s[index:new_index][::-1]:
                    recurse(new_index,current_words+[s[index:new_index]])
        recurse(0,[])
        return ans
'''
