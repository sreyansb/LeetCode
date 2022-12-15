#attempt1:
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def findAns(index1, index2):
            if index1 < 0 or index2 < 0:
                return 0
            if text1[index1] == text2[index2]:
                return 1+findAns(index1-1,index2-1)
            return max(findAns(index1-1,index2), findAns(index1, index2-1))
        return findAns(len(text1)-1, len(text2)-1)
