class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        @lru_cache(None)
        def findAns(index):
            if index >= n:
                return [[""]]
            ansLocal = []
            for nextIndex in range(index,n):
                word = s[index:nextIndex+1]
                if word != word[::-1]:
                    continue
                nextAns = findAns(nextIndex+1)
                for ans in nextAns:
                    ansLocal.append([word] + ans)
            return ansLocal
        
        ans = findAns(0)
        return [li[:-1] for li in ans]

                        
