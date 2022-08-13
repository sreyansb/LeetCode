#attempt2:
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        di = {}
        number_of_words = len(words)
        len_of_each_word = len(words[0])
        len_of_words = len_of_each_word*number_of_words
        for word in words:
            if word not in di:
                di[word] = 0
            di[word] += 1
        which_word_starts_at = [0]*len(s)
        for index in range(len(s)-len_of_each_word+1):
            word = s[index:index+len_of_each_word]
            if word in di:
                which_word_starts_at[index] = word
        ans = []
        for index in range(len(s)-len_of_words+1):
            seen = {}
            for no_of_words in range(number_of_words):
                word = which_word_starts_at[index+no_of_words*len_of_each_word]
                if word not in seen:
                    seen[word] = 0
                seen[word] += 1
            if seen == di:
                ans.append(index)
                
        return ans
            

#attempt1: WA
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_of_each_word = len(words[0])
        len_of_words = sum([len(word) for word in words])
        words = {word:index+1 for index,word in enumerate(words)}
        number_of_words = len_of_words//len_of_each_word
        which_word_starts_at = [-1]*len(s)
        for index in range(len(s)-len_of_each_word+1):
            word = s[index:index+len_of_each_word]
            if word in words:
                which_word_starts_at[index] = words[word]
        ans = []
        for index in range(len(s)-len_of_words+1):
            flag = True
            seen = {-1}
            for no_of_words in range(number_of_words):
                if which_word_starts_at[index+no_of_words*len_of_each_word] in seen:
                    flag = False
                seen.add(which_word_starts_at[index+no_of_words*len_of_each_word])
            if flag:
                ans.append(index)
        return ans
            
'''
