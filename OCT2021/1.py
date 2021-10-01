#attempt1: LCS
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def recurse(index1,index2):
            if index1<0 or index2<0:
                return 0
            if text1[index1]==text2[index2]:
                return 1+recurse(index1-1,index2-1)
            return max(recurse(index1,index2-1),recurse(index1-1,index2))
        return recurse(len(text1)-1,len(text2)-1)