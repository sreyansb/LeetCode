#attempt1:
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        di = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans = [""]
        for i in digits:
            nextans = []
            for alphabet in di[i]:
                for word in ans:
                    nextans.append(word+alphabet)
            ans = nextans
        return ans if ans[0] != "" else []
