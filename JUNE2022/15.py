#attempt3:
from collections import Counter
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))
        di = {}
        for word in words:
            wordlen = len(word)
            if wordlen not in di:
                di[wordlen] = []
            di[wordlen].append(word)
        
        graph = {}
        for word in words:
            graph[word] = []
            wordlen = len(word)
            if wordlen+1 in di:
                for word2 in di[wordlen+1]:
                    for index in range(wordlen):
                        index_in_word2 = word2.find(word[:index])
                        if index_in_word2 != -1 and word[index:] in word2[index_in_word2:]:
                            graph[word].append(word2)
                            break
        n = len(words)
        
        @lru_cache(None)
        def dfs(word):
            wordlen = len(word)
            ans = 1
            for nextword in graph[word]:
                ans = max(ans,1+dfs(nextword))
            #print(word,ans)
            return ans
        
        maxans = 1
        for word in words:
            maxans = max(maxans,dfs(word))
        return maxans
            
                        
                    
                    
                
