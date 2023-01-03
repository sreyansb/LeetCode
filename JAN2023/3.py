#attempt2:
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        colLength = len(strs[0])
        rowLength = len(strs)
        ans = 0
        for col in range(colLength):
            for row in range(1,rowLength):
                if strs[row][col] < strs[row-1][col]:
                    ans += 1
                    break
        return ans

#attempt1:
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columnWords = ["" for i in range(len(strs[0]))]
        for word in strs:
            for index,char in enumerate(word):
                columnWords[index] += char
        l = list(filter(lambda x: x != "".join(sorted(x)), columnWords))
        return len(l)
