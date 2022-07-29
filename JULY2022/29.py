#attempt1:
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            di_pattern_to_word = {}
            set_word_to_pattern = set()
            flag = True
            for index,char in enumerate(pattern):
                if char in di_pattern_to_word:
                    if di_pattern_to_word[char] != word[index]:
                        flag = False
                        break
                else:
                    if word[index] in set_word_to_pattern:
                        flag = False
                        break
                    di_pattern_to_word[char] = word[index]
                    set_word_to_pattern.add(word[index])
            if flag:
                ans.append(word)
        return ans
                
