#attempt1:
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache(None)
        def findlcs(index1,index2):
            if index1<0 or index2<0:
                return 0
            if word1[index1] == word2[index2]:
                return 1+findlcs(index1-1,index2-1)
            else:
                return max(findlcs(index1,index2-1),findlcs(index1-1,index2))
        
        return len(word1)+len(word2)-2*findlcs(len(word1)-1,len(word2)-1)
    
        
