#attempt2:TOOK HELP
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = set()
        word_index_map = {word:index for index,word in enumerate(words)}
        for index,word in enumerate(words):
            n = len(word)
            for prefix_index in range(n+1):
                if word[:prefix_index] == word[:prefix_index][::-1]:
                    first_word = word[prefix_index:][::-1]
                    if first_word in word_index_map:
                        ans.add((word_index_map[first_word],index))
            for suffix_index in range(n,-1,-1):
                if word[suffix_index:] == word[suffix_index:][::-1]:
                    first_word = word[:suffix_index][::-1]
                    if first_word in word_index_map:
                        ans.add((index,word_index_map[first_word]))
        return [i for i in ans if i[0]!=i[1]]
                    
        

#attempt1: TLE
'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        n = len(words)
        for index_word1 in range(n):
            for index_word2 in range(index_word1+1,n):
                new_word = words[index_word1]+words[index_word2]
                if new_word[::-1] == new_word:
                    ans.append([index_word1,index_word2])
                new_word = words[index_word2]+words[index_word1]
                if new_word[::-1] == new_word:
                    ans.append([index_word2,index_word1])
        return ans
'''
