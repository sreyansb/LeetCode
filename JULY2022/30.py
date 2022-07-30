#attempt3:
from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        combined_letter_count = {}
        for word in words2:
            di = Counter(word)
            for char in di:
                if char not in combined_letter_count:
                    combined_letter_count[char] = 0
                combined_letter_count[char] = max(combined_letter_count[char],di[char])
        ans = []
        for word in words1:
            di = Counter(word)
            flag = True
            for char in combined_letter_count:
                if char not in di or combined_letter_count[char] > di[char]:
                    flag = False
                    break
            if flag:
                ans.append(word)
        return ans
            
        

#attempt2: Go with max rather than combination
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        combined_letter_count = {}
        for word in words2:
            di = {}
            for char in word:
                if char not in di:
                    di[char] = 0
                di[char] += 1
            for char in di:
                if char not in combined_letter_count:
                    combined_letter_count[char] = 0
                combined_letter_count[char] = max(combined_letter_count[char],di[char])
        ans = []
        for word in words1:
            di = {}
            for char in word:
                if char not in di:
                    di[char] = 0
                di[char] += 1
            flag = True
            for char in combined_letter_count:
                if char not in di or combined_letter_count[char] > di[char]:
                    flag = False
                    break
            if flag:
                ans.append(word)
        return ans
            
        

#attempt1: WA
'''
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        combined_letter_count = {}
        for word in words2:
            for char in word:
                if char not in combined_letter_count:
                    combined_letter_count[char] = 0
                combined_letter_count[char] += 1
        ans = []
        for word in words1:
            di = {}
            for char in word:
                if char not in di:
                    di[char] = 0
                di[char] += 1
            flag = True
            for char in combined_letter_count:
                if char not in di or combined_letter_count[char] > di[char]:
                    flag = False
                    break
            if flag:
                ans.append(word)
        return ans
'''        
        
