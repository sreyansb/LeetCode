#attempt1:
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_di = {}
        for index,i in enumerate(s):
            if i not in letter_di:
                letter_di[i] = index
            else:
                letter_di[i] = -1
        for i in letter_di:
            if letter_di[i] != -1:
                return letter_di[i]
        return -1

        
